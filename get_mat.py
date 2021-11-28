from getplayer1 import player1
import time


def get_mat():
    while True:
        b = int(input("\n[1]Forage\n[2]Mine\n[3]Return"))
        if b == 1:
            for i in range(10, 0, -1):
                print("Foraging...")
                time.sleep(1)
                print(i)
            player1.wood = player1.wood + 10
            print("\nYou have " + str(player1.wood) + " wood planks.")
        elif b == 2:
            for i in range(30, 0, -1):
                print("Mining...")
                time.sleep(1)
                print(i)
            player1.stone = player1.stone + 10
            print("\nYou have " + str(player1.stone) + " pieces of stone.")
        elif b == 3:
            break
