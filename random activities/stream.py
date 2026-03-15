# # stream = open("text.txt")
# # print(stream.readlines())
# # # print(stream.readlines(20))
# # # print(stream.readlines(20))
# # # print(stream.readlines(20))
# # stream.close()

# from os import strerror

# try:
#     ccnt = lcnt = 0
#     s = open('text.txt', 'rt')
#     lines = s.readlines(-1)
#     print(lines)
#     while len(lines) != 0:
#         for line in lines:
#             lcnt += 1
#             for ch in line:
#                 print(ch, end='')
#                 ccnt += 1
#         lines = s.readlines(1)
#     s.close()
#     print("\n\nCharacters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))


# from os import strerror

# try:
#     ccnt = lcnt = 0
#     for line in open('text.txt', 'rt'):
#         print(line)
#         lcnt += 1
#         for ch in line:
#             print(ch, end=' ')
#             ccnt += 1
#     print("\n\nCharacters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))


# from os import strerror

# try:
# 	file = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
# 	for i in range(10):
# 		file.write("line #" + str(i+1) + "\n")
# 	file.close()
# except IOError as e:
# 	print("I/O error occurred: ", strerror(e.errno))
    
from os import strerror

# data = bytearray(10)

# try:
#     binary_file = open('file.bin', 'rb')
#     binary_file.readinto(data)
#     binary_file.close()

#     for b in data:
#         print(hex(b), end=' ')
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))
    


try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read())
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    
    
