N = 5
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
"""
# N = int(input())
# students = []

for item in range(N):
    name = str(input())
    rating = float(input())    
    students.append([name, rating])
"""    
print(students)

students.sort(key = lambda students: students[1])
print(students)

min_rating = students[0][1]

tmp_students = []
tmp_students = students
ratinge_student_2 = []

rating = min_rating
while rating == min_rating:
    tmp_students.pop(0)
    rating = tmp_students[0][1]   

min_rating = tmp_students[0][1]
for item, student in enumerate(tmp_students):
    if student[1] == min_rating:
        ratinge_student_2.append(student)
    
print(ratinge_student_2)
    
ratinge_student_2.sort(key = lambda students: students[0])

for student in ratinge_student_2:
    print(student[0])

    








