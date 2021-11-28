from getplayer1 import player1


def show_stats():
    while True:
        f = int(input("\n[1]Player Stats\n[2]Inventory Stats\n[3]Return"))
        if f == 1:
            print("\n" + str(player1))
        elif f == 2:
            inventory = [str(player1.wood) + " wood", str(player1.stone) + " stone"]
            print("\n")
            for i in inventory:
                print(i)

        elif f == 3:
            break
