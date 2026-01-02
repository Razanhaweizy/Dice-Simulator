import random

terminate = False

while not terminate:
    user_input = input("Roll the dice? ").lower()
    if user_input == "y":
        dices = int(input("How many dice to roll? "))
        rolls = []
        res = ""
        for i in range(dices):
            rand_roll = random.randint(1, 6)
            rolls.append(str(rand_roll))
        res.join(rolls)
        print(f'({", ".join(rolls)})')
    elif user_input == "n":
        print("Thanks for playing!")
        terminate = True
        continue
    else:
        print("Invalid choice :P")
        continue



