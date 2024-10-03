import random
# Welcome message and introduction
print("-----Welcome to the Head or Tail game--------")
python_pt = "pythonizer"
print(f"My name is: {python_pt}")
gamer = input("What is your name, my friend? \n")
print(f"Well, welcome dear: {gamer}")
print("Now let's play Head or Tail!!")
gamer_guess = input("Choose 'head' or 'tail': ").lower()  # Ensure the user input is lowercase for comparison
# Generate random guess for Pythonizer (0 for head, 1 for tail)
pythnizer_guess = random.randint(0, 1)  # This generates either 0 or 1
# Convert Pythonizer's guess to a readable format (string)
if pythnizer_guess == 0:
    pythnizer_choice = "head"
else:
    pythnizer_choice = "tail"
print(f"I choose: {pythnizer_choice}")
# Determine the outcome
if pythnizer_choice == gamer_guess:
    print("It's a tie! No winner this round.")
else:
    print("You win!") if pythnizer_choice != gamer_guess else print("I win!")
