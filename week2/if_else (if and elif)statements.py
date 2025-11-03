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
else:
 print("\n Not sure which direction to move!")
print()

# Ask user for a number
print("Please enter a whole number.")
number = int(input())
# Display relevant message
if number % 2 == 0:
 print(f"The number {number} is an even number.")
else:
 print(f"The number {number} is an odd number.")