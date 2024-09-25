# insert the ascii code when there is internet connection
print("Welcome to Treasure Island!")
print("Your mission is to find the Treasure.")
choise1 = input(" you\'r at a crossed, where do you want to go? type 'left' or 'right' ").lower()
if choise1 == "left":
    choise2 = input('you have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choise2 == "wait":
        chiose3 = input('you arrive at the island unharmed. There is a house with 3 doors. one red, one yellow one blue. Which color do you choose? ').lower()
        if chiose3 == 'red':
            print("it is full of fire. Game over!!!")
        elif chiose3 == 'yellow':
            print("You find the treasure!!! You win!!")
        elif chiose3 == 'blue':
            print("you enter room of beasts!!! Game over.")
        else:
            print("you choose a door that doesnt exist!!! Game over.")
    else:
        print("you got attacked by shark!! game over!!")
else:
    print("you fell in to a hole. Game over!!!")
# needs to debug not finished!!!

