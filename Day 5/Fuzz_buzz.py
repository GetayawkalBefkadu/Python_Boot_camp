# Fizz Buzz Game
# if number divisible by 3 print Fizz
# if number divisible by 5 print Buzz
# if number divisible by both 3 and 5 print Fizz Buzz
sum = 0
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("FizzBuzz")
    else:
        print(number)
