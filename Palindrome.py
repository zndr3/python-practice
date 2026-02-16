
class Palindrome:
    def __init__(self):
        self.__num = 0
        self.__numOriginal = 0
        self.__numReversed = 0
        self.__numPal = 0
    
    def __add(self):

        self.__numReversed += self.__numPal # print(f"numreversed + numpal {self.__numReversed}")

        if self.__num != 0:
            self.__numReversed *= 10

    def __result(self):

        if self.__numReversed == self.__numOriginal:
            print(f"{self.__numOriginal} is a palindrome")
        else:
            print(f"{self.__numOriginal} is not a palindrome")
        



    def __check(self):
        self.__numOriginal = 0
        self.__numReversed = 0
    

        self.__numOriginal += self.__num

        while self.__num > 0:
            self.__numPal = 0
            self.__numPal += self.__num % 10 # print(f"numpalindrome {self.__numPal}")
            self.__num -= self.__numPal # print(f"numoriginal - numpal {self.__num}")
            self.__num /= 10 # print(f"numoriginal / 10 {self.__num}")
            self.__add()
        else:
            self.__num = 0
            self.__result()

        
    def start(self):
        print("Palindrome Checker")
        print("Enter any key to exit....")

        while True:
            try:
                self.__num = int(input("\nEnter number to check: "))
                self.__check()
            except ValueError:
                exit("Bye!!.")

palindrome = Palindrome()

palindrome.start()