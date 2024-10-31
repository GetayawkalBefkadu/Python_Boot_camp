# testing random code challange
# Initial list
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# Step 1: Prompt the user to enter a number to replace the middle element
user_input = int(input("Enter a number to replace the middle element: "))

# Find the middle index
middle_index = len(hat_list) // 2

# Replace the middle element with the user input
hat_list[middle_index] = user_input

# Step 2: Remove the last element from the list
hat_list.pop()

# Step 3: Print the length of the modified list
print("Length of the list:", len(hat_list))

# Print the updated list
print("Updated list:", hat_list)


# Step 1: Create an empty list named beatles
beatles = []

# Step 2: Use the append() method to add the following members of the band to the list
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Step 3: Use a for loop and the append() method to prompt the user to add Stu Sutcliffe and Pete Best
for member in ["Stu Sutcliffe", "Pete Best"]:
    user_input = input(f"Add {member} to the band (yes/no): ").strip().lower()
    if user_input == "yes":
        beatles.append(member)
print("Step 3:", beatles)

# Step 4: Use the del instruction to remove Stu Sutcliffe and Pete Best from the list
del beatles[-2:]  # Remove the last two members
print("Step 4:", beatles)

# Step 5: Use the insert() method to add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Final Output
print("Final Beatles list:", beatles)

