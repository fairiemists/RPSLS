from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)


    def choose_gesture(self): 
        print()
        self.current_gesture = input(f"Enter your gesture choice: ")
        print(f"{self.name} picked {self.gestures[int(self.current_gesture)]}")
        
    