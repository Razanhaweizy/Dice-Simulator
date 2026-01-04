import random
from collections import Counter
from typing import List

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

def display_menu() -> None:
    print("* Type 'y' to roll a die")
    print("* Type 'n' to terminate the program")
    print("* Type 'c' to view how many dice you have rolled")
    print("* Type 's' to see the stats of your dice rolls")
    print("* Type 'h' to view a histogram of your dice rolls")
    return

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

#TODO add docstring
def draw_histogram(data, bar_char='*') -> None:
    freq_lst = []
    for tup in data:
        for i in range(tup[1]):
            freq_lst.append(tup[0])
            
    if len(freq_lst) == 0:
        print("You have not rolled any die ^_^ ")
        return
    
    counts = Counter(freq_lst)
    max_label_length = max(len(str(label)) for label in counts.keys())

    print("Histogram representation of dice roll frequencies: ")
    for label, count in sorted(counts.items()):
        bar = bar_char * count
        print(f"{str(label).rjust(max_label_length)} | {bar} ")
    

while not terminate:
    if dice_counter == 100:
        print("Wow, you're locked in... you have officially rolled 100 times")

    user_input = input("Roll the dice? Type m to view the menu :3 ").lower()

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
    elif user_input == "m":
        display_menu()
        continue
    elif user_input == "c":
        print(f"You have rolled {dice_counter} dices >_<")
        continue
    elif user_input == "s":
        display_stats()
        continue
    elif user_input == "h":
        draw_histogram(num_count.items())
    else:
        print("Invalid choice :P")
        continue

