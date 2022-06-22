

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.human = Human()
        self.ai = AI()

# if number of players = 1 or 2 create human player(s)
# if number of players = 0 or 1 create ai player(s)


player_one = Human(Player)
