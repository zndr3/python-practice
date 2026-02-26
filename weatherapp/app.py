from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'your_API_key'  # Replace with your OpenWeatherMap API key

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None
    if request.method == 'POST':
        city = request.form['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': data['name'],
                'temp': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed'],
                'icon': data['weather'][0]['icon'],
                'icon_url': f'http://openweathermap.org/img/wn/{data["weather"][0]["icon"]}@2x.png'
            }
        else:
            error = 'City not found. Please try again.'
    return render_template("index.html", weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True)
