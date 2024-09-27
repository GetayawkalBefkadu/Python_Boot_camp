# let us calculate your BMI(body mass index using if conditions!!!
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
    print("please start some sports and check your doctor please!!!")
else:
    print("Jesus Crist!!!!  You are Clinically obese!!!")
