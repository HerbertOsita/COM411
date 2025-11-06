print("What type of adventure should I have?")
adventure_type = input()

if (adventure_type == "scary") or (adventure_type == "short"):
    print("Entering the dark forest!")
elif (adventure_type == "safe") or (adventure_type == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")

print("\nWhat did I hear?")
hear = input()

print("What did I see")
see = input()

if (hear == "grr") and (see == "two red eyes"):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")