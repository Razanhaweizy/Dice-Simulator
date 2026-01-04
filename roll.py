import random
from collections import Counter
from typing import List

terminate = False
dice_counter = 0
die_face = 6 #default is 6

num_count = {}

stats_dict = {
    "sum_rolls": 0,
    "average": 0.0,
    "most_common": 0,
    "least_common": 0,
}

valid_faces = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]

def populate_dict():
    num_count.clear()
    for i in range(1, die_face + 1):
        num_count[i] = 0
    return

def reset_stats(user_reset=False) -> None:
    #only reset die face if user manually reset stats
    global die_face
    if user_reset:
        die_face = 6

    #reset dice counter
    global dice_counter
    dice_counter = 0
    #reset the stats dictionary
    stats_dict["average"] = 0.0
    stats_dict["least_common"] = 0
    stats_dict["most_common"] = 0
    stats_dict["sum_rolls"] = 0
    #reset the num_count dictionary
    populate_dict()
    return

#TODO add docstring
def display_menu() -> None:
    print("* Type 'y' to roll a die")
    print("* Type 'n' to terminate the program")
    print("* Type 'c' to view how many dice you have rolled")
    print("* Type 's' to see the stats of your dice rolls")
    print("* Type 'h' to view a histogram of your dice rolls")
    print("* Type 'f' to change the face of your die. The options are: d4, d6, d8, d10, d12, d20, d100 *NOTE* this will reset your stats, don't forget to save :)")
    print("* Type 'r' to reset your stats. This will also reset your chosen die face to default")
    return

#TODO add docstring
def get_die_face(choice: str) -> None:
    if not choice in valid_faces:
        print("Invalid die face choice @_@ ")
        return
    
    parsed = choice[1:]
    face_num = int(parsed)
    global die_face
    die_face = face_num
    reset_stats()
    print(f"You have successfully changed the die face to be {face_num}")
    populate_dict()
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
#once face is changed, maybe clear stats?
def update_stats(roll: int):
    num_count[roll] += 1 
    stats_dict["sum_rolls"] += roll
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
    

populate_dict()

while not terminate:
    if dice_counter == 100:
        print("Wow, you're locked in... you have officially rolled 100 times")

    user_input = input("Roll the dice? Type m to view the menu :3 ").lower()
    if user_input == "y":
        dices = get_valid_int("How many dice to roll? ")
        rolls = []
        for i in range(dices):
            dice_counter += 1 #track num of dice rolls
            rand_roll = random.randint(1, die_face) #roll a die
            #stats updates
            update_stats(rand_roll)
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
        continue
    elif user_input == "f":
        new_face = input("What face would you like your die to have? ")
        get_die_face(new_face)
        continue
    elif user_input == "r":
        reset_stats(True)
        continue
    else:
        print("Invalid choice :P")
        continue

