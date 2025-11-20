def observed ():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations

def run_task1 ():
    obs = observed()
    print (obs)

#run_task1 ()

def observed_items ():
    observations = []
    for i in range (7):
        user_input = input("please enter a observations")
        observations.append(user_input)
    return observations

def run_task2 ():
    print ("Counting observations...")
    obs = observed_items()
    obs_set = set()
    for o in obs:
        count = (o, obs.count(o))
        obs_set.add(count)

    print (obs_set)

run_task2()

def observed():
    observations = []

    for count in range(5):
        print("Please enter an observation:")
        observations.append(input())

    return observations

def remove_observations(observations):
    is_running = True

    while (is_running):
        print("Do you wish to remove an observation (yes/no)?")
        response = input()

        if (response == "yes"):
            print("Please enter the observation you wish to remove")
            observation = input()
            observations.remove(observation)
        else:
            is_running = False


def run_task3():
    observations = observed()
    remove_observations(observations)

    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    for data in sorted(observations_set):
        print(f"{data[0]} observed {data[1]} times.")

run_task3()

def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences
def run():
    print(pattern())

run()

def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences
def display_keys(data):
    print("Keys:")
    for key in data:
        print(key)
    print()

def display_values(data):
    print("Values:")
    for value in data.values():
        print(value)
    print()


def display_pairs(data):
    print("Pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")
    print()


def run():
    data = pattern()
    print(f"Dictionary:\n{data}")

    display_keys(data)
    display_values(data)
    display_pairs(data)

run()

def short_pattern():
    pattern = {"sequence":"101", "occurrences":5}
    return pattern

def medium_pattern():
    pattern = {"sequence":"111000", "occurrences":25}
    return pattern

def long_pattern():
    pattern = {"sequence":"1100110011001100", "occurrences":50}
    return pattern

def run_task3():
    print("Analysing patterns...")
    patterns = {
        "short sequence":short_pattern(),
        "medium sequence":medium_pattern(),
        "long sequence":long_pattern()
    }

    for key, value in patterns.items():
      print(f"{key}: {value}")

run_task3()

