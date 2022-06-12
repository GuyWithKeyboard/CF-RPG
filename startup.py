import pickle
import time
print("Hello!")
print("Welcome to micro rpg.")
name = str(input("What is your name?"))
print("Welcome, " + name + "!")
time.sleep(1)
gender = 0

while gender != "boy" or gender != "girl":
    gender = str(input("Are you a boy or a girl?"))
    if gender == "boy" or gender == "girl":
        break
    else:
        print("Please enter 'boy' or 'girl'.")

time.sleep(0.5)
print("Start by gathering materials and selling them!")
time.sleep(1)
print("It is slow at first, but you will get faster with experience.")
time.sleep(1.5)

ng = [name, gender]
pickle.dump(ng, open("variables.dat", "wb"))
