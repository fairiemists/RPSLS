from human import Human
from ai import AI


class Game: 
    def __init__(self, name):
        self.name = name
        self.player_one = None
        self.player_two = None


    def welcome(self):
        # general rules
        print(f"Welcome to Rock, Paper, Scissors, Lizard, Spock.")
        print()
        print(f"Each game will have three rounds.")
        print(f"First player to win two rounds wins the game.")
        print()
        print(f"Keep in mind...")
        print()
        # list of what beats what
        print(f"Rock crushes Scissors")
        print(f"Scissors cuts Paper")
        print(f"Paper covers Rock")
        print(f"Rock crushes Lizard")
        print(f"Lizard poisons Spock")
        print(f"Spock smashes Scissors")
        print(f"Scissors decapitates Lizard")
        print(f"Lizard eats Paper")
        print(f"Paper disproves Spock")
        print(f"Spock vaporizes Rock")


    def player_choice(self):
        # 0, 1, 2
        print(f"You can have up to two players. (0, 1, 2)")
        number_of_players = input("How many players? ")
        #create players
        if number_of_players == "0":
            print(f"You have chosen to have the computer play against itself.")
            print()
            self.player_one = AI("Player One")
            self.player_two = AI("Player Two")
        elif number_of_players == "1":
            print(f"You have chosen to play against the computer.")
            print()
            self.player_one = Human("Player One")
            self.player_two = AI("Player Two")
        elif number_of_players == "2":
            print(f"You have chosen to play against another person.")
            print()
            self.player_one = Human("Player One")
            self.player_two = Human("Player Two")
        else: 
            print("I did not understand that response. Please choose from the following options.")
            return self.player_choice()
        pass




    def choose_gesture(self):

        self.player_one.choose_gesture()
        self.player_two.choose_gesture()

        if self.player_one.current_gesture == self.player_two.current_gesture:
            print()
            print(f"It's a tie! Both players picked {self.player_one.current_gesture}. ")

        elif self.player_one.current_gesture == self.player_one.gestures[0]: #Rock
            if self.player_two.current_gesture == self.player_two.gestures[1]:
                print()
                print(f"Paper covers Rock. Player Two wins!")
                self.player_two.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[2]:
                print()
                print(f"Rock crushes Scissors. Player One wins!")
                self.player_one.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[3]:
                print()
                print(f"Rock crushes Lizard. Player One wins!")
                self.player_one.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[4]:
                print()
                print(f"Spock vaporizes Rock. Player Two wins!")
                self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gestures[1]: #Paper
            if self.player_two.current_gesture == self.player_two.gestures[0]:
                print()
                print(f"Paper covers Rock. Player One wins!")
                self.player_one.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[2]:
                print()
                print(f"Scissors cuts Paper. Player Two wins!")
                self.player_two.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[3]:
                print()
                print(f"Lizard eats Paper. Player Two wins!")
                self.player_two.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[4]:
                print()
                print(f"Paper disproves Spock. Player One wins!")
                self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gestures[2]: #Scissors
            if self.player_two.current_gesture == self.player_two.gestures[0]:
                print()
                print(f"Rock crushes Scissors. Player Two wins!")
                self.player_two.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[1]:
                print()
                print(f"Scissors cuts Paper. Player One wins!")
                self.player_one.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[3]:
                print()
                print(f"Scissors decapitates Lizard. Player One wins!")
                self.player_one.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[4]:
                print()
                print(f"Spock smashes Scissors. Player Two wins!")
                self.player_two.score += 1

        elif self.player_one.current_gesture == self.player_one.gestures[3]: #Lizard
            if self.player_two.current_gesture == self.player_two.gestures[0]: #Rock
                print()
                print(f"Rock crushes Lizard. Player Two wins!")
                self.player_two.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[1]: #Paper
                print()
                print(f"Lizard eats Paper. Player One wins!")
                self.player_one.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[2]: #Scissors
                print()
                print(f"Scissors decapitates Lizard. Player Two wins!")
                self.player_two.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[4]: #Spock
                print()
                print(f"Lizard poisons Spock. Player One wins!")
                self.player_one.score += 1

        elif self.player_one.current_gesture == self.player_one.gestures[4]: #Spock
            if self.player_two.current_gesture == self.player_two.gestures[0]: #Rock
                print()
                print(f"Spock vaporizes Rock. Player One wins!")
                self.player_one.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[1]: #Paper
                print()
                print(f"Paper disproves Spock. Player Two wins!")
                self.player_two.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[2]: #Scissors
                print()
                print(f"Spock smashes Scissors. Player One wins!")
                self.player_one.score += 1
            elif self.player_two.current_gesture == self.player_two.gestures[3]: #Lizard
                print()
                print(f"Lizard poisons Spock. Player Two wins!")
                self.player_two.score += 1
        
        print()
        print(f"Player One's score is {self.player_one.score}.")
        print(f"Player Two's score is {self.player_two.score}.")
        print()

        pass


    def big_hooray(self):
        print(f"Hooray!")
        if self.player_one.score >= 2:
            print(f"Player One wins the game!")
        elif self.player_two.score >= 2:
            print(f"Player Two wins the game!")

        pass

    def run_game(self):
        print()
        self.welcome()
        print()
        self.player_choice()

        while self.player_one.score <= 1 and self.player_two.score <=1:
            self.choose_gesture()
        print()
        self.big_hooray()

        print()
        user_input = input("Would you like to play again? y/n ")
        print()
        if user_input == "y":
            self.run_game()
        else:
            print(f"Thank you for playing Rock, Paper, Scissors, Lizard, Spock!")
            
        pass


