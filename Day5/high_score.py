student_scores = [100, 78, 65, 89, 86, 55, 91, 64, 89]

higher_score = 0

for score in student_scores:
    if score > higher_score:
        higher_score = score
    else:
        pass
print(higher_score)