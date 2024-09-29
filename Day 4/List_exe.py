import random
# List_of_names = input("Give the list of names separated by comma. ")
# names = List_of_names.split(",")
# name_items = len(names)
# random_choice = random.randint(0,name_items -1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + " is going to pay to days meal!! ")
# ----------------- another method ---------------------------------
List_of_names = input("Give the list of names separated by comma. ")
names = List_of_names.split(",")
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to pay to days meals!!")
