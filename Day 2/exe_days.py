# calculating how many das, weeks and month you used in your life-time so far
day = 1
weeks = 7 * int(day)
month = 12 * int(day)
year = 365 * int(day)
age = int(input("what is your current age: "))
used_day = age * year
used_weeks = age * weeks
used_month = age * month
print(f"your have been uesd: {used_day} days,{used_weeks} weeks and  {used_month} months  ")
