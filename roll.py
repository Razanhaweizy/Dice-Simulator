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

def calculate_stats():
    print(stats_dict)

while not terminate:
    if dice_counter == 50:
        print("Wow, you're locked in... you have officially rolled 100 times")

    user_input = input("Roll the dice? Type c to view amount of dice rolled. s for stats ").lower()

    if user_input == "y":
        dices = int(input("How many dice to roll? "))
        rolls = []
        for i in range(dices):
            dice_counter += 1 #track num of dice rolls
            rand_roll = random.randint(1, 6) #roll a die
            #stats updates
            num_count[rand_roll] += 1 
            stats_dict["sum_rolls"] += rand_roll
            stats_dict["average"] = stats_dict["sum_rolls"] / dice_counter

            #fix logic
            stats_dict["most_common"] = max(num_count.values())
            stats_dict["least_common"] = min(num_count.values())
            
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
        calculate_stats()
        continue
    else:
        print("Invalid choice :P")
        continue

