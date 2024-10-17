# python function
success = ""  # Initially, success is not achieved

def success_console():
    while success == "":  # While success is not achieved
        print("Work hard, try again")  # Motivational message
        # Simulating hard work to achieve success
        break  # You can remove this break to allow multiple attempts
    else:
        print("Congratulations! Enjoy your success!")  # Success message

# Simulate the process of achieving success
success = "achieved"  # Set success once achieved
success_console()

        
def my_function():
    print("----------------------Hello!!----------------------")
    print("====================================================")
my_function()
# Function to calculate the square of a number
def calculate_square(number):
    # The function accepts one argument 'number'
    # It returns the square of that number
    return number * number

# Interactive part: Asking the user for input
num = int(input("Enter a number to find its square: "))

# Calling the function with user's input and displaying the result
print("The square of", num, "is", calculate_square(num))
# ---------------------------------------------------------------------
# Function to check if a number is even or odd
def check_even_odd(number):
    # If number is divisible by 2 with no remainder, it's even
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Interactive input: Asking the user to input a number
num = int(input("Enter a number to check if it's even or odd: "))

# Calling the function and displaying the result
print(f"The number {num} is {check_even_odd(num)}.")
