from sunau import AUDIO_FILE_ENCODING_LINEAR_16
from human import Human
from ai import AI


class Game: 
    def __init__(self, name):
        self.name = name
        self.player_one = None
        self.player_two = None


    def welcome(self):
        # general rules
        print()
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
        print()


    def player_choice(self):
        # 0, 1, 2
        print()
        print(f"You can have up to two players. (0, 1, 2)")
        number_of_players = input("How many players? ")
        #create players
        if number_of_players == "0":
            print(f"You have chosen to have the computer play against itself.")
            self.player_one = AI("Player One")
            self.player_two = AI("Player Two")
        elif number_of_players == "1":
            print(f"You have chosen to play against the computer.")
            self.player_one = Human("Player One")
            self.player_two = AI("Player Two")
        elif number_of_players == "2":
            print(f"You have chosen to play against another person.")
            self.player_one = Human("Player One")
            self.player_two = Human("Player Two")
        else: 
            print("I did not understand that response. Please choose from the following options.")
            return self.player_choice()


    def choose_gesture(self):
        #different functions for player 1 & 2? ...I don't think so.
        #pull from Human or AI
        #display round winner (or tie)
        #change score
        #next round prompt?
        pass

    def winner_check(self):
        #check for game winner
            #is player wins at least 2 and more than the other player?
                #YES: Announce winner. Move on to Big Hooray.
                #NO: Go to gesture_codes then repeat choose_gesture.        # 
        pass

    def big_hooray(self):
        #offer to play again
        pass

    def run_game(self):
        print()
        self.welcome()
        print()
        self.player_choice()