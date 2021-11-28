import pickle
import os.path
from player import Player
if str(os.path.exists("player1.dat")) == "True":
    print("Found previous data!")
    player1 = pickle.load(open("player1.dat", "rb"))
else:
    ng = pickle.load(open("variables.dat", "rb"))
    name = ng[0]
    gender = ng[1]
    player1 = Player(name, gender, 0, 0, 0, 0, 0)
