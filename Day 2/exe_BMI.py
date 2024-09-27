# Calculating BMI(Body mass index)
height = float(input("insert your height \n"))
weight = float(input("insert your weight \n"))
BMI = weight / (height * height)
if 18 <= BMI <= 25:
    print("You Body Mass Index is:  " + str(BMI) + "and it is normal!!")
elif BMI < 18:
    print("You Body Mass Index is:  " + str(BMI) + "and it is low BMI!!")
elif BMI > 25:
    print("You Body Mass Index is:  " + str(BMI) + "and high BMI You should see a doctor or work some workout!! ")
else:
    print("Inter a correct information please !!")

