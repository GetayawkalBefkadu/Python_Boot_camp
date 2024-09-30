import random
print("-----Wellcome to Head or tail game--------")
python_pt = "pythonizer"
print(f"my name is: {python_pt}" )
gamer = input("what is your name my friend? \n")
print(f"well wellcome dear: {gamer}")
print("Now choose Head or tail?")
gamer = input()
random_gusse = random.randint(0,1 )
if random_gusse == 0:
    print("Head")
else:
    print("Tail")
if random_gusse == gamer:
    print("same choise no winner")
elif random_gusse != gamer:
    print("You win")
# i want to create head or tail game using random module but it is not finished and i will fix it.
