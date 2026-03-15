# from os import strerror

class StudentsDataException(Exception):
    pass

# class BadLine(StudentsDataException):
#     pass

class FileEmpty(StudentsDataException):
    def __init__(self, message):
        # self.message = message
        super().__init__(message)
    

def start():
    try:
        file = input("Enter file name: ")
        # file = "samplefile2.txt"
        print(file)
        stream = open(file)
        if stream.read():
            stream.seek(0)
            data = {}
            for line in stream:
                line = line.split()
                # print(line)
                full_name = line[0] + " " + line[1]
                if full_name in data.keys():
                    data[full_name] += float(line[2])
                else:
                    data[full_name] = float(line[2])
                # print(data)
            stream.close()
            for student in sorted(data.keys()):
                print(student, "-> ", data[student])
        else:
            # print("File name is empty")
            raise FileEmpty("File is empty")
        
    except FileEmpty as e:
        print(e)

    except Exception as e:
        print(e.strerror, ":", e.filename)

while True:
    start()
        

