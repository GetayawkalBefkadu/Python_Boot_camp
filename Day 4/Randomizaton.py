# when i use random (built in)  for the first time my file name was random.py
# which results name conflict and take me   a long time to find out the error!!
import random
random_int = random.randint(1,100)
print(f"i am just generating random integer:- {random_int}")
print("=================================================")
random_float = random.random() # this will generate random number but will not take any argument!! 
print(f"i am just generating random integer:- {random_float}")
