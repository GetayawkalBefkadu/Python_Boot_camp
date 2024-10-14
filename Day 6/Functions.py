# python function
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
