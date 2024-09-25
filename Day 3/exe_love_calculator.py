print("welcome to Love calculator!! ")
name1 = input("what is your name?:  ")
name2 = input("what is their name?: ")
combined_name = name1 + name2
lower_case = combined_name.lower()
t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")
true = t + r + u + e
l = name1.count("l")
o = name1.count("o")
v = name1.count("v")
e = name1.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print(f"your love score is: {love_score}%, you together  is like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"your love score is: {love_score}%, you alright together!.")
else:
    print(f"your love score is: {love_score}%")


