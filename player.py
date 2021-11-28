class Player:

    def __init__(self, name, gender, level, balance, wood, stone, exp):
        self.name = name
        self.gender = gender
        self.level = level
        self.balance = balance
        self.wood = wood
        self.stone = stone
        self.exp = exp

    def __repr__(self):
        player_string = self.name + "\n" + self.gender + "\n" + "$" + str(self.balance) + "\n" + "Level " + str(
            self.level)
        return player_string
