import random

terminate = False

while not terminate:
    user_input = input("Roll the dice?").lower()
    if user_input == "y":
        roll_x = random.randint(1, 6)
        roll_y = random.randint(1, 6)
        print(f'({roll_x}, {roll_y})')
    elif user_input == "n":
        print("Thanks for playing!")
        terminate = True
        continue
    else:
        print("Invalid choice :P")
        continue



