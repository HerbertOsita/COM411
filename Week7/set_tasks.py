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