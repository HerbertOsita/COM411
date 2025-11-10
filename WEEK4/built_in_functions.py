print("Program Started!")
print("Please enter a standard character:")
character = input()

if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("A single character was expected.")
print("Program Ended!")


print("Program Started!")

print("Please enter an ASCII code:")
code = int(input())

if code >= 32 and code <= 126:
    print(f"The character represented by the ASCII value {code} is: {chr(code)}")
else:
    print("The character cannot be displayed.")

print("Program Ended!")

def listen():

    print("What sound did you hear?")
    sound = input()

    print(f"That was a loud {sound}!")

listen()

def Identity():
    print("What lies before us?")
    response = input()

    if response == "a large boulder":
        print("it's time to run!")
    else:
        print("We will be fine.")

identify = ()

def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("Not sure about that plan")

escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")

def cross_bridge(steps):
    for step in range(steps):
        print("Crossed step.")

    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

cross_bridge(3)
cross_bridge(6)

def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")

climb_ladder(5, 2)
climb_ladder(2, 5)

def display_ladder(steps):
    for step in range(steps):
        print("| |")
        print("***")

    print("| |")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

create_ladder()

def sum_weights(person_weight, inventory_weight):
    total_weight = person_weight + inventory_weight
    return total_weight

def calc_avg_weight(person_weight, inventory_weight):
    avg_weight = sum_weights(person_weight, inventory_weight) / 2
    return avg_weight

def run():
    print("What is the weight of the person?")
    person_weight = float(input())

    print("What is the weight of their inventory?")
    inventory_weight = float(input())

    print("What would you like to calculate (sum or average)?")
    action = input()

    if action == "sum":
        answer = sum_weights(person_weight, inventory_weight)
        print(f"The sum of weights is {answer:.2f}")
    elif action == "average":
        answer = calc_avg_weight(person_weight, inventory_weight)
        print(f"The average weight is {answer:.2f}")
    else:
        print("I am not sure what you would like to do.")

run()

def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print(f"| {word} |")
    print("-" * num_dashes)

def display_lower_case(word):
    print(word.lower())

def display_upper_case(word):
    print(word.upper())

def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")

def display_repeated(word):
    print("How many times should the word be displayed?")
    repetitions = int(input())

    for repetition in range(repetitions):

        if (repetition % 2 == 0):
            print(display_lower_case(word))

        else:
            print(display_upper_case(word))

def run():
    print("Please enter a word:")
    word = input()

    print("What would you like to do with this word?")
    print("[1] Display in a box")
    print("[2] Display lower-case")
    print("[3] Display upper-case")
    print("[4] Display mirrored")
    print("[5] Display repeated")
    print("[6] Quit")

    response = int(input())

    if response == 1:
        display_box(word)
    elif response == 2:
        display_lower_case(word)
    elif response == 3:
        display_upper_case(word)
    elif response == 4:
        display_mirrored(word)
    elif response == 5:
        display_repeated(word)
    else:
        print("Unknown option.")

run()

import random

print("Please enter the minimum value:")
min_value = int(input())

print("Please enter the maximum value:")
max_value = int(input())

random_number = random.randrange(min_value, max_value)

print(f"I am thinking of a number between {min_value} and {max_value}.")
print("Can you guess what it is?")

guessed_correctly = False

while not guessed_correctly:
    print("Please enter a number:")
    guess = int(input())

    if guess == random_number:
        print("Congratulations! You guessed the correct answer!")
        guessed_correctly = True
    elif guess < random_number:
        print("Guess higher")
    else:
        print("Guess lower")

print("Game over!")

import random

print("Please enter the minimum value:")
min_value = int(input())

print("Please enter the maximum value:")
max_value = int(input())

random_number = random.randrange(min_value, max_value)

print(f"I am thinking of a number between {min_value} and {max_value}.")
print("Can you guess what it is?")

while(True):
    print("Please enter a number:")
    guess = int(input())

    if guess == random_number:
       print("Congratulations! You guessed the correct answer!")
       break
    elif guess < random_number:
        print("Guess higher")
    else:
        print("Guess lower")

print("Game over!")
