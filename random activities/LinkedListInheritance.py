import sys
sys.stdout.reconfigure(encoding='utf-8')

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next = None
        
        
        
class LinkedListTrain:
    
    def __init__(self):
        self.head = None
        
    def add_car(self,car_name):
        
        new_car = Node(car_name)
        if not self.head:
            self.head = new_car
        
        else:
            current=self.head
            while current.next:
                current = current.next
            current.next = new_car
            
    def remove_car(self):
        if not self.head:
            print("no cars to remove")
            return
        if not self.head.next:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        
    def display_train(self):
        if not self.head:
            print("The train has no cars!")
            return
        current = self.head
        cars=[]
        while current:
            cars.append(current.data)
            current = current.next
        print("Train Structure " + "->".join(cars))
        
class Train(LinkedListTrain):
    def __init__(self):
        super().__init__()
    
    def board_passengers(self):
        print("Passengers are boarding the train")
        
class RollerCoaster(LinkedListTrain):
    def __init__(self):
        super().__init__()
        
    def start_ride(self):
        print("The roller coaster ride is starting! Hold on tight!")
        
        
print("\n Standard Train:")
train = Train()
train.add_car("🚂Engine")
train.add_car("🚃Passenger Car 1")
train.add_car("🚃Passenger Car 2")
train.display_train()
train.board_passengers()



print("\n Roller Coaster")
coaster = RollerCoaster()
coaster.add_car("Front Car")
coaster.add_car("Middle Car")
coaster.add_car("Back Car")
coaster.display_train()
coaster.start_ride()