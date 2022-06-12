from fight import fight
from get_mat import get_mat
from shop import shop
from show_stats import show_stats
from stop import stop
from getplayer1 import player1
import os.path


# this lets the player know they have previous data.
if str(os.path.exists("player1.dat")) == "True":
    print("\n" + str(player1))

# this is the main menu
# it will loop forever
while True:
    a = input("\n[1]Show Stats\n[2]Gather Materials\n[3]Shop\n[4]Fight\n[5]Stop")
    # this is the prompt
    if a == "1":
        show_stats()
    elif a == "2":
        get_mat()
    elif a == "3":
        shop()
    elif a == "4":
        fight()
    elif a == "5":
        stop()
        break
