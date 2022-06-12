from getplayer1 import player1
import time


def get_mat():
    while True:
        b = input("\n[1]Forage\n[2]Mine\n[3]Return")
        if b == "1":
            for i in range(10, 0, -1):
                print("Foraging...")
                time.sleep(1)
                print(i)
            player1.materials["wood"] = player1.materials["wood"] + 10
            player1.exp = player1.exp + 5
            print("\nYou have " + str(player1.materials["wood"]) + " wood planks.")
        elif b == "2":
            for i in range(30, 0, -1):
                print("Mining...")
                time.sleep(1)
                print(i)
            player1.materials["stone"] = player1.materials["stone"] + 10
            player1.exp = player1.exp + 15
            print("\nYou have " + str(player1.materials["stone"]) + " pieces of stone.")
        elif b == "3":
            break
