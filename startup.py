import pickle
print("Hello!")
print("Welcome to micro rpg.")
name = str(input("What is your name?"))
print("Welcome, " + name + "!")

gender = 0

while gender != "boy" or gender != "girl":
    gender = str(input("Are you a boy or a girl?"))
    if gender == "boy" or gender == "girl":
        break
    else:
        print("Please enter 'boy' or 'girl'.")

ng = [name, gender]
pickle.dump(ng, open("variables.dat", "wb"))
