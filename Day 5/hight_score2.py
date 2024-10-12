# Initialize an empty list to store the student scores
student_scores = []  # Keep the list for storing the scores

# Ask for the number of students (this should not overwrite the list)
num_students = int(input("Insert the number of students: \n"))

# Use a for loop to collect student scores
for i in range(num_students):
    # Ask for each student's score and convert it to an integer
    score = int(input(f"Enter the score for student {i + 1}: "))
    # Append the score to the list
    student_scores.append(score)

# Initialize the variable to store the highest score
highest_score = 0

# Use a for loop to find the highest score in the list
for score in student_scores:
    if score > highest_score:  # Check if the current score is higher than the highest so far
        highest_score = score  # Update the highest score if a larger score is found

# Display the highest score
print(f"The highest score is {highest_score}")
