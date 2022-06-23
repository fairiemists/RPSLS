from human import Human
from ai import AI


class Game: 
    def __init__(self, name) -> None:
        self.name = name
        self.player_one = ()
        self.player_two = ()


    def welcome():
        # general rules
        # list of what beats what
        pass

    def player_choice():
        # 0, 1, 2
        #create players
        pass

    def choose_gesture():
        #different functions for player 1 & 2? ...I don't think so.
        #pull from Human or AI
        #print gesture codes
        #display gesture choices
        #display round winner (or tie)
        #change score
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