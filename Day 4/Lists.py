# -----------------who let us develop who will pay game!!!----------------------

import random

# Welcome Message
print("==============================|")
print("|         Welcome to          |")
print("|       Who Will Pay Game!    |")
print("|=============================|")

# Ask the user if they want to start the game
choice = input("Are you ready? (Yes or No): ").strip().lower()

if choice == "yes":
    # Get the list of names from the user
    List_of_names = input("Give the list of names separated by commas (e.g., John, Sarah, Bob): \n").strip()

    # Split the input string into a list of names and remove any extra spaces around each name
    names = [name.strip() for name in List_of_names.split(",")]

    if len(names) > 1:  # Ensure there are at least two names
        # Randomly choose a person who will pay
        person_who_will_pay = random.choice(names)

        # Display the result
        print(f"\n🎉 Congratulations! {person_who_will_pay} is going to pay for today's meal! 🎉\n")
    else:
        print("Please enter more than one name to play the game.")
else:
    print("Okay, think it over and come back later. Thank you!!!")

