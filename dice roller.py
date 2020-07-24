import random

run = True
while run:
    dice = random.randint(1, 6)
    if dice == 1:
        print(" ___________ ")
        print("|           |")
        print("|     .     |")
        print("|           |")
        print("|___________|")
    elif dice == 2:
        print(" ___________ ")
        print("|  .        |")
        print("|           |")
        print("|        .  |")
        print("|___________|")
    elif dice == 3:
        print(" ___________ ")
        print("|  .        |")
        print("|     .     |")
        print("|        .  |")
        print("|___________|")
    elif dice == 4:
        print(" ___________ ")
        print("|  .     .  |")
        print("|           |")
        print("|  .     .  |")
        print("|___________|")
    elif dice == 5:
        print(" ___________ ")
        print("|  .     .  |")
        print("|     .     |")
        print("|  .     .  |")
        print("|___________|")
    elif dice == 6:
        print(" ___________ ")
        print("|  .     .  |")
        print("|  .     .  |")
        print("|  .     .  |")
        print("|___________|")

    play = str(input("Would You Like To Roll Again: ").lower())
    if play == "yes":
        run = True
    else:
        run = False
