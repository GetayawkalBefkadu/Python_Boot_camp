# prime number checker
def prime_number():
    number = int(input("Insert any number: "))
    is_prime = True
    for i in range(2 , number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("The number you Enter is prime number")
    else:
        print("The number you Enter is not prime number")
prime_number()
