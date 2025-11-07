print("How many apples should I remove?")
apples_to_remove = int(input())

apples_removed = 0

print()


while apples_removed < apples_to_remove:
    print("Remove apple.")
    apples_removed = apples_removed + 1

print("\nHow many obstacles should I avoid?")
obstacles_to_avoid = int(input())

obstacles_avoided = 0

print()

while obstacles_avoided < obstacles_to_avoid:
    print("Avoiding...", end="")
    obstacles_avoided = obstacles_avoided + 1
    print(f"Done! {obstacles_avoided} obstacles avoided.")

print("\nHow many bars should be charged?")
bars_to_charge = int(input())

bars_charged = 0

print()

while bars_charged < bars_to_charge:
 bars_charged = bars_charged + 1
 print(f"Charging: {'█' * bars_charged}")

print("The battery is fully charged.")

print("\nPlease enter a phrase?")
phrase = input()

hellos = 0
print()

while hellos < len(phrase):
 print("Hi ", end="")
 hellos = hellos + 1

print("Calculating the sum of the first 100 numbers...")

number = 1

total = 0

while number <= 100:
 total = total + number
 number = number + 1

print(f"...Done! The answer is {total}")

print("How many numbers should I sum up?")
number_to_sum = int(input())

summed = 0

print()

total = 0

while summed < number_to_sum:
        print(f"Please enter number {summed} of {number_to_sum}:")
        number = int(input())
        total = total + number
        summed = summed + 1

print(f"The answer is {total}.")

print("How many mountains should I display?")
mountains = int(input())

print("Displaying....")

for mountain in range(mountains):
  print("""
        _
       / \
      /^  \ 
     /  ^  \ 
   _/ ^ ^  ^ \
  /  ^     ^  \ 
  
  """)

print("How far are we from the target?")
distance = int(input())

print()

for count in range(distance, 0, -1):
    print(f"{count} steps remaining")

print("Target achieved!")

print("\nWhat level of brightness is required?")
brightness_desired = int(input())

print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_desired + 1, 2):
    print(f"Brightness level: {'*' * brightness}")

print("Complete!")

print("What word do you see?")
word = input()

print("\nDisplaying index positions...\n")

for count in range(0, len(word), 1):
  print(f"index {count}:", word[count])

print("What phrase do you want to see in reverse?")
phrase = input()

print("\nReversing...")
print("The phrase is ", end="")

for position in range(len(phrase) - 1, -1, -1):
 print(phrase[position], end="")

print("\nWhat phrase do you see?")
phrase = input()

print("\nOutputting...")
print("The phrase is:")

for letter in phrase:
 print(letter)

print("\nHow many rows should I have?")
rows = int(input())

print("\nHow many columns should I have?")
columns = int(input())

for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print()

print("\nPlease enter a sequence:")
sequence = input()

print("\nPlease enter the character for the marker:")
marker = input()

marker1_position = -1
marker2_position = -1

for position in range(0, len(sequence), 1):
    letter = sequence[position]

    if letter == marker:
        if (marker1_position == -1):
            marker1_position = position
        else:
            marker2_position = position

print(f"The distance between the markers is {marker2_position -
marker1_position - 1}.")

print("\nPlease enter a sequence:")
sequence = input()

print("\nPlease enter the character for the marker:")
marker = input()

is_counting = False
count = 0

for character in sequence:
    if (is_counting == False) and (character == marker):
        print("Found first marker")
        is_counting = True
    elif (is_counting == True) and (character == marker):
        print("Found last marker")
    elif is_counting:
        count += 1

print(f"\nThe distance between the markers is {count}")