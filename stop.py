import pickle
import time
from getplayer1 import player1


def stop():
    pickle.dump(player1, open("player1.dat", "wb"))
    print("Stopping...")
    time.sleep(0.5)
