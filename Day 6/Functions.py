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

# d/f functions examples
# =====================================================================
def greet(name):
  """Greets a person by name.

  Args:
    name: The name of the person to greet.
  """

  print("Hello, " + name + "!")

greet("Alice")
# =====================================================================
def calculate_area(length, width):
  """Calculates the area of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The area of the rectangle.
  """

  area = length * width
  return area

result = calculate_area(5, 10)
print("The area is:", result)
# =====================================================================
def greet(name, greeting="Hello"):
  """Greets a person with a customizable greeting.

  Args:
    name: The name of the person to greet.
    greeting: The greeting message (default: "Hello").
  """

  print(greeting + ", " + name + "!")

greet("Bob")  # Output: Hello, Bob!
greet("Charlie", "Hi")  # Output: Hi, Charlie!
# =====================================================================
def factorial(n):
  """Calculates the factorial of a number.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

result = factorial(5)
print("Factorial of 5 is:", result)
# =====================================================================
def sum_numbers(*args):
  """Calculates the sum of a variable number of numbers.

  Args:
    *args: A variable number of arguments.

  Returns:
    The sum of the arguments.
  """

  total = 0
  for num in args:
    total += num
  return total

result = sum_numbers(1, 2, 3, 4, 5)
print("Sum of numbers:", result)
# =====================================================================

