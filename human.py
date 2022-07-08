from player import Player
import time

class Human(Player):
    def __init__(self, name):
        super().__init__(name)


    def choose_gesture(self): 
        print()
        time.sleep( 0.5 )
        print(f"Press 1 for {self.gestures[0]}")
        time.sleep( 0.5 )
        print(f"Press 2 for {self.gestures[1]}")
        time.sleep( 0.5 )
        print(f"Press 3 for {self.gestures[2]}")
        time.sleep( 0.5 )
        print(f"Press 4 for {self.gestures[3]}")
        time.sleep( 0.5 )
        print(f"Press 5 for {self.gestures[4]}")
        time.sleep( 0.5 )
        print()
        
        user_input = input(f"Enter your gesture choice: ")
        if user_input == "1":
            self.current_gesture = self.gestures[0]
        elif user_input == "2":
            self.current_gesture = self.gestures[1]
        elif user_input == "3":
            self.current_gesture = self.gestures[2]
        elif user_input == "4":
            self.current_gesture = self.gestures[3]
        elif user_input == "5":
            self.current_gesture = self.gestures[4]
        else:
            print(f"I didn't understand that. Please choose a gesture from the list.")
            time.sleep( 0.5 )
            return self.choose_gesture()
        print()
        print(f"{self.name} picked {self.current_gesture}")
        
    