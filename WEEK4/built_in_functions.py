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
