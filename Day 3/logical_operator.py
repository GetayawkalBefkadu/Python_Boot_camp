print("welcome to Rollercoaster! ")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("you have to pay 5$")
    elif age <= 18:
        bill = 7
        print("You have to pay 7$")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You have free ticket, enjoy!!")
    else:
        bill = 12
        print("You have to pay 12$")
    wants_photo = input("Do you want photo? Y or N ?")
    if wants_photo == "Y":
      bill += 3

    print(f"The value of the bill is {bill}")
else:
    print("sorry you have to grow taller before you can ride.  ")