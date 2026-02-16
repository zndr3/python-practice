
import math
import random
import datetime
import sqlite3
import json

num_runners = 5

runners = []

for i in range(num_runners):

    name = f"Runner_{i+1}"

    finish_time_min = round(random.uniform (30, 70), 2)

    speed_kph = 10 / (finish_time_min / 60)

    raw_pace = finish_time_min / 10

    pace_min_per_km = math.ceil(raw_pace * 100) / 100

    stamina_score = round(1000 / math.pow(finish_time_min, 2), 2)

    runner = {

        "name": name,

        "finish_time": finish_time_min,

        "speed": round (speed_kph, 2),

        "pace": pace_min_per_km,

        "stamina": stamina_score
    }
    runners.append(runner)

conn = sqlite3.connect("runners.db")

cursor = conn.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS run_event ( id INTEGER PRIMARY KEY AUTOINCREMENT, event_date TEXT, runner_data TEXT )''')

event_date = datetime.datetime.now().isoformat()
for runner in runners:
    runner_json = json.dumps(runner)
    cursor.execute("INSERT INTO run_event (event_date, runner_data) VALUES (?, ?)", (event_date, runner_json))

conn.commit()


print(f"\n 10KM FUN RUN EVENT 57 {datetime.datetime.now().strftime('%B %d, %I:%M %p')}\n")
cursor.execute("SELECT runner_data FROM run_event WHERE event_date = ?", (event_date,))
results = cursor.fetchall()

fastest_runner = None

for row in results:
    data = json.loads(row[0])

    print(f"Name        : {data['name']}")
    print(f"Finish Time : {data['finish_time']} minutes")
    print(f"Speed       : {data['speed']} km/h")
    print(f"Pace        : {data['pace']} min/km")
    print(f"Stamina     : {data['stamina']} \n")

    if fastest_runner is None or data['finish_time'] <fastest_runner['finish_time']:
        fastest_runner = data
    elif math.isclose(data['finish_time'], fastest_runner['finish_time'], abs_tol=0.1):
        print(f" Tie detected between {data['name']} and {fastest_runner['name']}")

if fastest_runner:
    print(f"Fastest Runner: {fastest_runner['name']} with a time of {fastest_runner['finish_time']} minutes!")

conn.close()
