# Initialize an empty list to store student scores
student_scores = []

# Get the number of students/scores from the user
num_students = int(input("Enter the number of students: "))

# Collect scores from the user and store them in the list
for i in range(num_students):
    score = float(input(f"Enter the score for student {i + 1}: "))  # Asking user for score input
    student_scores.append(score)  # Append the score to the list

# Initialize the variable to store the highest score
highest_score = student_scores[0]  # Assume the first score is the highest initially

# Loop through the list to find the highest score
for score in student_scores:
    if score > highest_score:  # Check if the current score is higher than the highest score so far
        highest_score = score  # Update the highest score if a larger one is found

# Display the highest score
print("\nThe highest score is:", highest_score)
