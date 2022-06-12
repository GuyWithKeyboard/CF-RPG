import math


class Player:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.level = 0
        self.balance = 0
        self.exp = 0
        self.materials = {"wood": 0, "stone": 0}

    def __repr__(self):
        player_string = self.name + "\n" + self.gender + "\n" + "$" + str(self.balance) + "\n" + "Level " + str(
            math.floor(self.level))
        return player_string
