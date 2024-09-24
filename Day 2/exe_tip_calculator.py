print("welcome to the tip calculator:")
bill = float(input("what was the total bill? $"))
tip = float(input("what percentage would you like to give? 10,12 or 15? "))
people = int(input("how many people to split the bill? "))
bill_with_tip = tip/100 * bill + bill
total_bill = bill_with_tip / people
round(total_bill,2 )
print(f"your total bill is {total_bill} each!!")
