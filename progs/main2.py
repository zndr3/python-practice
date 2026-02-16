# # import sys

# # # note the double backslashes!
# # sys.path.append("C:\\Users\\ZNDRS\\Desktop\\ALL FILES\\Python Files\\packages")


# def mysplit(strng):
    
#     strng = strng.strip()
    
#     my_list = []
    
#     if strng:
#         new_str = ""
#         for ch in strng + " ":
#             if ch.isspace():
#                 my_list.append(new_str)
#                 new_str = ""
#             else:
#                 new_str += ch
#         return my_list
#     else:
#         return my_list


# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))
tup = (1,2,3)
print(type(tup))
