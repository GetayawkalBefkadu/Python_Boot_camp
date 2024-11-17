def greet(): # normal function without parameter
    print("i choose python")
    print("and the javascript")
    print("finally became a software engineer!!!")
greet()
# ---------------let us see functions with parameter and argument
def greeting(name):
    print(f"hello dear {name}")
    print(f"Thank you for learning python  {name}")
greeting("Getayawkal ")
# ------------------------------------------------------------
def BMI():
    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms (kg): \n"))
    height = float(input("Enter your height in meters (m): \n"))

    # Calculate BMI
    bmi = weight / height ** 2

    # Display BMI
    print(f"Your BMI is {bmi:.2f}")

    # Provide feedback based on BMI value
    if bmi < 18.5:
        print("You have a lower BMI. Consider improving your eating habits!")
    elif 18.5 <= bmi < 25:
        print("Congrats! Your BMI is normal. Keep it up!")
    elif bmi >= 25:
        print("Warning: Your BMI indicates overweight. It's time to start exercising!")
BMI()
# ----------------------------------------------------------
def Triangle():
    base = float(input("Insert base of the triangle : \n"))
    height = float(input("Insert height of the triangle : \n"))
    tri = 0.5 * base * height
    print(f"The are of triangle is : {tri}")
Triangle()
# ---------------------------------------------------------------
