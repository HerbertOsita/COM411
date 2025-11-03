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


 # Ask user for the direction
 print("\nPlease enter the first number.")
 first_number = int(input())
 print("Please enter the second number.")
 second_number = int(input())
 # Determine which message to display
 if first_number < second_number:
     print("The first number is the smallest.")
 elif first_number > second_number:
     print("The second number is the smallest.")
 else:
     print("The two numbers are equal.")

# Ask user for numbers
print("\nPlease enter the first whole number?")
first_number = int(input())
print("Please enter the second whole number?")
second_number = int(input())
print("Please enter the third whole number?")
third_number = int(input())
even_numbers = 0
odd_numbers = 0
# Determine which numbers are even and which are odd
if first_number % 2 == 0:
 even_numbers = even_numbers + 1
else:
 odd_numbers = odd_numbers + 1
if second_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
 odd_numbers = odd_numbers + 1
if third_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
print(f"There were {even_numbers} even and {odd_numbers} odd numbers.")

