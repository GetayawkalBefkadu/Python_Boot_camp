height = float(input("Insert your height: "))
weight = float(input("Insert your weight: "))
BMI = weight / (height * height)
if BMI <= 18.5:
     print(f"Your BMI is: {BMI} - under weight")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is: {BMI} -  Normal")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is: {BMI} -  Over weight")
elif BMI > 30 and  BMI < 35:
    print(f"Your BMI is: {BMI} -  Obese")
else:
    print("You are Clinically obese!!!")
