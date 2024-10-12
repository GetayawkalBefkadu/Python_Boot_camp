student_score = []
student_score = int(input("Insert student score: \n"))
higest_score = 0
for score in student_score:
    if score > higest_score:
        higest_score =score
print(f"The highest score is {higest_score}")