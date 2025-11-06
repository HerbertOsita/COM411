print("What type of cover does this book have")
cover_type = input ()

if cover_type == "soft":
    print ("Is the book perfect-bound?")
    perfect_bound = input ()

    if perfect_bound == "yes":
        print ("soft cover, perfect bound books are very popular!")
    else:
        print ("soft covers with coils or stitches are great for short books")
else:
    print ("Books with hard covers can be more expensive!")

print("\nWhere should I look?")
place = input()

if place == "in the bedroom":
 print("Where in the bedroom should I look?")
 bedroom_place = input()

 if bedroom_place == "under the bed":
     print("Found some shoes but no phone.")
else:
     print("Found some shoes but no phone.")

if place == "in the bathroom":
    print ("Where in the bathroom should I look?")
    bathroom_place = input()

    if bathroom_place == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found some stuff but no phone.")

elif place == "in the living room":
    print("Where in the living room should I look?")
    lab_place = input()

    if lab_place == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")

else:
    print("I am not sure where that place is located.")