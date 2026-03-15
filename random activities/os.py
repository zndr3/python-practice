
import os
import platform
print(platform.uname())

# courses = ["c" , "cpp" , "python"]

# for dir in courses:
#     dirs = ["c" , "cpp" , "python"]
#     dirs.remove(dir)
#     for other_dir in dirs:
#         os.makedirs("tree/" + dir + "/other_courses/" + other_dir)


def find(path , directory):
    os.chdir(os.getcwd() + "/" + path)
    
    # print("current dir: " , os.getcwd())
    # print("path list dir: " , os.listdir(path))
    
    if directory in os.listdir(os.getcwd()):
        print("course dir: " , os.getcwd().replace('\\', '/') + "/" + directory)

    if os.listdir(os.getcwd()):
        for dir in os.listdir(os.getcwd()):
            find(dir , directory)
        else:
            os.chdir("../")
            return
    else:
        # print("current dir: " , os.getcwd())
        os.chdir("../")
        return 

path = input("Enter path name: ")
directory = input("Enter directory name: ")

find(path , directory)

    