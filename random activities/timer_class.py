class Timer:
    def __init__(self, hrs = 0, mins = 0, secs = 0):
        self.__hrs = hrs
        self.__mins = mins
        self.__secs = secs

    def __str__(self):
        if self.__hrs in range(10):
            self.__hrs = f"0{self.__hrs}"
        if self.__mins in range(10):
            self.__mins = f"0{self.__mins}"
        if self.__secs in range(10):
            self.__secs = f"0{self.__secs}"
            
        return f"{self.__hrs} : {self.__mins} : {self.__secs}"

    def next_second(self):
        if int(self.__secs) + 1 == 60:
            self.__secs = 0
            if int(self.__mins) + 1 == 60:
                self.__mins = 0
                if int(self.__hrs) + 1 == 24:
                    self.__hrs = 0
                else:
                    self.__hrs += 1
            else:
                self.__mins += 1
        else:
            self.__secs += 1
            
    def prev_second(self):
        if int(self.__secs) - 1 == -1:
            self.__secs = 59
            if int(self.__mins) - 1 == -1:
                self.__mins = 59
                if int(self.__hrs) - 1 == -1:
                    self.__hrs = 23
                else:
                    self.__hrs -= 1
            else:
                self.__mins -= 1
        else:
            self.__secs -= 1

timer = Timer(23, 56, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
        