import math

from getplayer1 import player1


def show_stats():
    player1.level = player1.exp / 100
    while True:
        f = input("\n[1]Player Stats\n[2]Level Progress\n[3]Inventory Stats\n[4]Return")
        if f == "1":
            print("\n" + str(player1))
        elif f == "2":
            print("level " + str(math.floor(player1.level)) + "\n" + str(player1.exp) + "/100 exp")
        elif f == "3":
            inventory = [str(player1.materials["wood"]) + " wood", str(player1.materials["stone"]) + " stone"]
            print("\n")
            for i in inventory:
                print(i)

        elif f == "4":
            break
