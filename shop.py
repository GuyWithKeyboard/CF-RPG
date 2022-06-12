from getplayer1 import player1

def promptForSellQuantity(material):
    prompt = "\nHow many stacks of %s would you like to sell?" % (material,)
    while True:
        answer = input(prompt)
        try:
            quantity = int(answer)
            assert quantity > 0
            break
        except ValueError:
            print("Must be an integer.")
        except AssertionError:
            print("Must be greater than 0.")
    return quantity

def sellTransaction(material, amount, value):
    if amount * 10 > player1.materials[material]:
        print("\nYou don't have enough %s. A stack is 10 pieces." % (material,))
    else:
        player1.materials[material] = player1.materials[material] - amount * 10
        earnings = amount * 10 * value
        player1.balance = player1.balance + earnings
        print("\n-" + str(amount * 10) + " %s" % (material,))
        print("\n+$" + str(amount * 10 * value))

def shop():
    while True:
        c = input("\n[1]Sell\n[2]Trade\n[3]Return")
        while c == "1":
            d = input("\n[1]Sell wood\n[2]Sell stone\n[3]Return")
            if d == "1":
                e = promptForSellQuantity("wood")
                sellTransaction("wood", e, 1)
            if d == "2":
                e = promptForSellQuantity("stone")
                sellTransaction("stone", e, 3)
            if d == "3":
                c = "0"
        if c == "2":
            print("\nYou cannot trade at this time.")
            c = "0"
        if c == "3":
            break
