print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("what size pizza do you want? S , M , L  \n")
add_pepperoni = input("Do you want peperoni? Y , N \n")
extra_cheese = input("Do you want extra cheese? Y , N \n")
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill +=2
    if extra_cheese == "Y":
        bill +=1
elif size == "M":
    bill =  20
    if add_pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 1
print(f"Your final bill is ${bill}")

