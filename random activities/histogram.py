from os import strerror

try:
    letter = [chr(i) for i in range(ord("a") , ord("z") + 1)]

    file = input("Enter file name: ")
    # file = "samplefile.txt"
    stream = open(file)
    counts = {}
    for ch in stream.read().lower():
        # print(ch)
        if ch in counts.keys():
            counts[ch] += 1
        else:
            check = letter.count(ch.lower())
            counts[ch.lower()] = check
    stream.close()
    stream = open(file + ".hist" , "wt")
    for key in sorted(counts.keys() , key = lambda x: counts[x] , reverse=True):
        stream.write(key + "-> " + str(counts[key]) + "\n")
        # print(key," -> ", counts[key])
    stream.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))