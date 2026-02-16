import random

class SlotMachine:
    def __init__(self):
        self.__symbols = ["😂","❤️","😒","😁","😘","9️⃣"]
        self.__jackpot = [["😂","😂","😂"] , ["❤️","❤️","❤️"] , ["😒","😒","😒"] , ["😁","😁","😁"] , 
                          ["😘","😘","😘"] , ["9️⃣","9️⃣","9️⃣"]]
        self.__slots = ["","",""]
        self.__token = 15

    def __spin(self):
        self.__slots = [random.choice(self.__symbols) for _ in range(3)]
        print("🧱 |"," | ".join(self.get_slots())," | 🧱")

        if self.__slots in self.__jackpot:
            self.__winner()
        
    def __minus(self):
        self.__token -= 1

    def __gameOver(self):
        # quit()
        exit("Game Over!")
    
    def __winner(self):
        # quit()
        exit("Jackpot! Congratulations")

    def start(self):
        while self.__token > 0:
            print(f"You have {self.__token} tokens left")
            input("Press enter to continue...")
            self.__minus()
            self.__spin()
            self.start()
        else:
            print(f"You have {self.__token} tokens left")
            self.__gameOver()            

    def get_slots(self):
        return self.__slots

slotmachine = SlotMachine()

slotmachine.start()

