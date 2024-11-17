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
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')
    # --------------------------------------------------------------
