# average height calculator
print("Welcome to the Average Student Height Calculator!")

# Get user input and split it into a list of heights
student_heights = input("Please enter a list of student heights in centimeters, separated by spaces: ").split()

# Convert each height from string to integer
for i in range(len(student_heights)):
    student_heights[i] = int(student_heights[i])

# Calculate the total height using a for loop
total_heights = 0
for height in student_heights:
    total_heights += height

# Calculate the average height
average_height = total_heights / len(student_heights)

# Display the result
print(f"\nThe total height of students is: {total_heights} cm")
print(f"The average height is: {average_height:.2f} cm")
