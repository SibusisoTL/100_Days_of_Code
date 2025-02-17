#For Loop

Student_Scores = [10, 142, 120,171, 184, 149, 24, 9, 8, 199, 78,89,86]
max_score = 0
for score in Student_Scores:
    if score > max_score:
        max_score=score
print(max_score)