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
       / \\_
      /^  \ \
     /  ^  \ \_
   _/ ^ ^    ^\\
  /  ^     ^   \\
  
  """)
