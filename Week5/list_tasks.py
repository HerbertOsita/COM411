def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def run():
    print(directions())

if __name__ == "__main__":
    run()

#Without Loop
def movements():
 path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3,
"Move Right", 1]
 return path
def run():
 print("Moving...")
 path = movements()
 print(f"{path[0]} for {path[1]} steps")
 print(f"{path[2]} for {path[3]} steps")
 print(f"{path[4]} for {path[5]} steps")
 print(f"{path[6]} for {path[7]} steps")
if __name__ == "__main__":
 run()

#With index-based for loop
def movements():
 path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3,
"Move Right", 1]
 return path
def run():
 print("Moving...")
 path = movements()
 for index in range(0, len(path), 2):
     print(f"{path[index]} for {path[index+1]} steps")

def movements():
 path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3,
"Move Right", 1]
 return path
def run():
    print("Moving...")
    path = movements()
    for index in range(0, len(path), 2):
     print(f"{path[index]} for {path[index+1]} steps")

if __name__ == "__main__":
    run()

def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    dirs = directions()
    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")

def run():
    menu()

if __name__ == "__main__":
    run()

def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    dirs = directions()
    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")
    index = int(input())
    return dirs[index]

def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"Escape route: {route}")

if __name__ == "__main__":
 run()

def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)

def run():
    print(f"Minimum likelihood of falling: {likelihood()}%")

if __name__ == "__main__":
    run()

def likelihood():
 likelihoods = (50, 38, 27, 99, 4)
 return min(likelihoods), max(likelihoods)

def run():
    probabilities = likelihood()
    print(f"Minimum likelihood of falling: {probabilities[0]}%")
    print(f"Maximum likelihood of falling: {probabilities[1]}%")

if __name__ == "__main__":
    run()

def steps():
    all_steps = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return all_steps

def run():
    all_steps = steps()
    good_steps = []
    bad_steps = []

    for step in all_steps:
        if (step[1] >= 50):
            bad_steps.append(step)
        else:
            good_steps.append(step)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

if __name__ == "__main__":
    run()


