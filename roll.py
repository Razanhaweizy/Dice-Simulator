import random
from collections import Counter
import os
import json

terminate = False
dice_counter = 0
die_face = 6 #default is 6
file_path = "./save.txt"

#dict that tracks the number of times a die digit is rolled
num_count = {}

#dict that tracks certain stats of all dies rolled
stats_dict = {
    "sum_rolls": 0,
    "average": 0.0,
    "most_common": 0,
    "least_common": 0,
}

#a list that tracks all the valid faces that this die can have
valid_faces = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]

def populate_dict() -> None:
    '''Helper function that populates the num_count dictionary with default (0) values
    depending on the face of the die .
    Example: d10 die will have keys 1-10 with value 0.'''
    num_count.clear()
    for i in range(1, die_face + 1):
        num_count[i] = 0
    return

def reset_stats(user_reset=False) -> None:
    '''Helper function that resets all stats (dice_counter, num_count, and stats_dict)
    to their default values which are 0.
    Param user_reset: default false. If true, means that user requested reset so the die
    face will also be reset. If false, used in changing die face to reset all values except
    die face.'''
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

def display_menu() -> None:
    '''Helper function that prints out all menu options (features) to the terminal'''
    print("* Type 'y' to roll a die.")
    print("* Type 'n' to terminate the program. *Note* your progress will be automatically saved.")
    print("* Type 'c' to view how many dice you have rolled.")
    print("* Type 's' to see the stats of your dice rolls.")
    print("* Type 'h' to view a histogram of your dice rolls.")
    print("* Type 'f' to change the face of your die. The options are: d4, d6, d8, d10, d12, d20, d100 *NOTE* this will reset your stats, don't forget to save :)")
    print("* Type 'r' to reset your stats. This will also reset your chosen die face to default.")
    print("* Type 'v' to save your progress.")
    print("* Type 'l' to load your most recent save. This will delete unsaved progress.")
    return

def get_die_face(choice: str) -> None:
    '''Helper function that updates the die face to the user's choosing and
    resets other stats
    Param choice: the user's input which represents what die face they want'''
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

def get_valid_int() -> int:
    '''Helper function that asks and parses the user's option for how many die to roll
    and validates the input
    Catches incorrect input and asks user to re-enter in that case'''
    while True:
        dices = input("How many dice to roll? ")
        try:
            dices_valid = int(dices)
            if dices_valid <= 0:
                print("Dice roll can't be 0 or negative, try again =)")
                continue
            return dices_valid
        except ValueError:
            print("Invalid number, please enter a valid integer -_-")
           
def update_stats(roll: int) -> None:
    '''Helper function that updates the tracked stats after every die roll'''
    num_count[roll] += 1 
    stats_dict["sum_rolls"] += roll
    stats_dict["average"] = stats_dict["sum_rolls"] / dice_counter
    max_val = max(num_count.values())
    min_val = min(num_count.values())
    stats_dict["most_common"] = [key for key, value in num_count.items() if value == max_val]
    stats_dict["least_common"] = [key for key, value in num_count.items() if value == min_val]
    return

def display_stats() -> None:
    '''Helper function that prints to terminal the current stats'''
    print(f"The sum of all rolls is: {stats_dict['sum_rolls']}")
    print(f"The average across all rolls is: {stats_dict['average']}")
    print(f"The most common value(s) rolled is: {stats_dict['most_common']}")
    print(f"The least common value(s) rolled is: {stats_dict['least_common']}")
    return

def draw_histogram(data, bar_char='*') -> None:
    '''Helper function that draws a histogram that shows frequency of each number
    rolled
    Param data: List of tuples where each tuple represents value and its frequency
    Param bar_char: Char used to represent frequency, optional. Default value: * '''
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
    return
    
#TODO add docstring
def save_progress() -> None:
    if not os.path.exists(file_path):
        open(file_path, "x")

    save_data = {
        "dice_counter": dice_counter,
        "die_face": die_face,
        "stats_dict": stats_dict,
        "num_count": num_count
    }

    with open(file_path, "w") as save_file:
        json.dump(save_data, save_file)

    print("Your progress have been saved >.< ")
    return

#TODO add docstring
def load_save() -> None:
    if not os.path.exists(file_path):
        print("No save file found.. ")
        return
    
    global dice_counter
    global num_count
    global stats_dict
    global die_face

    try:
        with open(file_path, "r") as save_file:
            save_data = json.load(save_file)
            
            dice_counter = save_data["dice_counter"]
            num_count = save_data["num_count"]
            stats_dict = save_data["stats_dict"]
            die_face = save_data["die_face"]

            num_count = {int(k): v for k, v in num_count.items()}

            print("Successfully loaded save :D")
    except (json.JSONDecodeError, KeyError) as error:
        print("Unfortunaley did not load the save...")
        print("Starting clean")
    return

populate_dict() #populate dict before starting
load_save()

#main program loop
while not terminate:
    if dice_counter == 100:
        print("Wow, you're locked in... you have officially rolled 100 times")

    user_input = input("Roll the dice? Type m to view the menu :3 ").lower()
    if user_input == "y":
        dices = get_valid_int()
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
        save_progress()
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
    elif user_input == "v":
        save_progress()
        continue
    elif user_input == "l":
        load_save()
        continue
    else:
        print("Invalid choice :P")
        continue

