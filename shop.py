from getplayer1 import player1


def shop():
    c = int(input("\n[1]Sell\n[2]Buy\n[3]Return"))
    while True:
        if c == 1:
            d = int(input("\n[1]Sell wood\n[2]Sell stone\n[3]Return"))
            if d == 1:
                e = -1
                while e < 0:
                    e = int(input("\nHow many stacks of wood would you like to sell?"))
                if e*100 > player1.wood:
                    print("\nYou don't have enough wood.")
                elif e*100 <= player1.wood:
                    player1.wood = player1.wood - e*100
                    earnings = e*100
                    player1.balance = player1.balance + earnings
                    print("\n-" + str(e*100) + " wood planks")
                    print("\n+$" + str(e*100))
            if d == 2:
                e = -1
                while e < 0:
                    e = int(input("\nHow many stacks of stone would you like to sell?"))
                if e*100 > player1.stone:
                    print("\nYou don't have enough stone.")
                elif e*100 <= player1.stone:
                    player1.stone = player1.stone - e*100
                    earnings = e*100*3
                    player1.balance = player1.balance + earnings
                    print("\n-" + str(e*100) + " pieces of stone")
                    print("\n+$" + str(e*100*3))
            if d == 3:
                c = 0
        if c == 2:
            print("\nYou cannot buy at this time.")
            c = 0
        if c == 3:
            break
