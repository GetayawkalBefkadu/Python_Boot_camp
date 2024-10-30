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
