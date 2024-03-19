student_heights = [180, 124, 165, 173, 189, 169, 146]

total = 0
number_of_students = len(student_heights)

for height in student_heights:
  total += height

average = round(total / number_of_students)

print(f"total height = {total}\nnumber of students = {number_of_students}\naverage height = {average}")