import random

terminate = False
dice_counter = 0

num_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

stats_dict = {
    "sum_rolls": 0,
    "average": 0.0,
    "most_common": 0,
    "least_common": 0,
}

#TODO add docstring
def get_valid_int(prompt: str) -> int:
    while True:
        dices = input("How many dice to roll? ")
        try:
            dices_valid = int(dices)
            return dices_valid
        except ValueError:
            print("Invalid number, please enter a valid integer -_-")
           
#TODO add docstring
def update_stats():
    num_count[rand_roll] += 1 
    stats_dict["sum_rolls"] += rand_roll
    stats_dict["average"] = stats_dict["sum_rolls"] / dice_counter
    max_val = max(num_count.values())
    min_val = min(num_count.values())
    stats_dict["most_common"] = [key for key, value in num_count.items() if value == max_val]
    stats_dict["least_common"] = [key for key, value in num_count.items() if value == min_val]

#TODO add docstring
def display_stats():
    print(f"The sum of all rolls is: {stats_dict['sum_rolls']}")
    print(f"The average across all rolls is: {stats_dict['average']}")
    print(f"The most common value(s) rolled is: {stats_dict['most_common']}")
    print(f"The least common value(s) rolled is: {stats_dict['least_common']}")

while not terminate:
    if dice_counter == 100:
        print("Wow, you're locked in... you have officially rolled 100 times")

    user_input = input("Roll the dice? Type c to view amount of dice rolled. s for stats ").lower()

    if user_input == "y":
        dices = get_valid_int("How many dice to roll? ")
        rolls = []
        for i in range(dices):
            dice_counter += 1 #track num of dice rolls
            rand_roll = random.randint(1, 6) #roll a die
            #stats updates
            update_stats()
            #add roll to result
            rolls.append(str(rand_roll))
        print(f'({", ".join(rolls)})')
    elif user_input == "n":
        print("Thanks for playing!")
        terminate = True
        continue
    elif user_input == "c":
        print(f"You have rolled {dice_counter} dices >_<")
        continue
    elif user_input == "s":
        display_stats()
        continue
    else:
        print("Invalid choice :P")
        continue

