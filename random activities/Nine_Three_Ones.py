
class Nine_Threes_Ones:
    def __init__(self, __num):
        self.__num = __num
        self.__one = 0
        self.__threes = 0
        self.__nines = 0

        while self.__num >= 9 and self.__num < 27:
            self.__nines += self.__num // 9
            self.__num -= 9 * self.__nines
        
        while self.__num < 9 and self.__num >= 3:
            self.__threes += self.__num // 3
            self.__num -= 3 * self.__threes

        while self.__num > 0:
            self.__one += self.__num // 1
            self.__num -= self.__one

        self.answer = f"nines : {self.__nines}, threes : {self.__threes}, ones : {self.__one}"

        return print(self.answer)
    
nine_threes_one = Nine_Threes_Ones(20)
print("🧱🧱🧱🧱")