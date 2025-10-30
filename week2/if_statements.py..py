print("What type of book is this?")
Book = input()
print()
if Book == "adventure":
    print (f"I like {Book} books!")

print("\nFinished reading book.")
print ()

print ("Please enter the activity to be performed.")
activity = input()
print()
if activity == "calculate":
    print ("performing calculations.....")
print()
print ("Activity completed!")

print("Towards which direction should I go (up, down, left or right)?")
direction = input()
print ()

if direction == "up":
    print(f"I am moving in an {direction}ward direction!")
elif direction == "down":
    print(f"I am moving in an {direction}ward direction!")
if direction == "left":
    print(f"I am moving in a {direction} direction!")
elif direction == "right":
    print(f"I am moving in a {direction} direction!")

