# # Caesar cipher.

# while True:
#     try:
#         text = input("Enter your message: ")
#         shift = int(input("Enter shift value from 1-25: "))
#         if 0 < shift < 26:
#             cipher = ''
#             for char in text:
#                 if char.isupper():
#                     if ord('A') <= shift + ord(char) <= ord('Z'):
#                         cipher += chr(shift + ord(char))
#                     else:
#                         cipher += chr(64 + ((ord(char) + shift) - ord('Z')))
#                 elif char.islower():
#                     if ord('a') <= shift + ord(char) <= ord('z'):
#                         cipher += chr(shift + ord(char))

#                     else:
#                         cipher += chr(96 + ((ord(char) + shift) - ord('z')))
#                 else:
#                     cipher += char
#             print(cipher)
#         else:
#             print("Please enter value from 1-25.")
#     except ValueError:
#         print("Please enter valid value from 1-25.")
    
# while True:
#     text = input("Enter text for palindrome check: ")
#     text = text.replace(" " , "")
#     text = text.lower()
#     new_text = ""
#     for i in range(len(text)-1, -1, -1):
#         new_text += text[i]
#     if new_text == text:
#         print("It's a palindrome")
#     else:
#         print("It's not a palindrome")
# while True:
#     text1 = input("Enter first text: ")
#     text2 = input("Enter second text: ")
#     text1 = "".join(sorted(list(text1.lower().replace(" ",""))))
#     text2 = "".join(sorted(list(text2.lower().replace(" ",""))))
#     if text1 == text2:
#         print("They're anagrams")
#     else:
#         print("They're Not anagrams")

while True:
    try:
        date = int(input("Enter birthdate with numbers only: "))
        new_date = 0
        while date not in range(10):
            while date != 0:
                minus = date % 10
                new_date += minus
                date = (date - minus) // 10
                print(minus, new_date, date)
            else:
                print("finished iteration" , minus, new_date, date)
                date = new_date
        else:
            break
    except ValueError:
        print("Enter numbers only")


while True:
    try:
        date = int(input("Enter birthdate with numbers only: "))
        date = str(date)
        new_date = 0
        while new_date not in range(1,10):
            new_date = 0
            for ch in date:
                new_date += int(ch)
            else:
                date = str(new_date)
        else:
            print("Digit of Life is:" , date)

    except ValueError:
        print("Enter numbers only")
        

        
