from human import Human
from ai import AI


class Game: 
    def __init__(self, name):
        self.name = name
        self.player_one = None
        self.player_two = None


    def welcome():
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
        print()


    def player_choice():
        # 0, 1, 2
        number_of_players = input("How many players? ")
        #create players
        pass

    def choose_gesture():
        #different functions for player 1 & 2? ...I don't think so.
        #pull from Human or AI
        #print gesture codes
        #display gesture choices
        #display round winner (or tie)
        #change score
        #next round prompt?
        pass

    def winner_check():
        #check for game winner
            #is player wins at least 2 and more than the other player?
                #YES: Announce winner. Move on to Big Hooray.
                #NO: Go to gesture_codes then repeat choose_gesture.        # 
        pass

    def big_hooray():
        #offer to play again
        pass