"""
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
"""

# N = int(input())
# students = []

# N = 3
# students = [['Krishna', '67', '68', '69'], ['Arjun', '70', '98', '63'], ['Malika', '52', '56', '60']]
N = 2
students = [['Harsh', '25', '26.5', '28'], ['Anurag', '26', '28', '30']]

"""
for item in range(N):
    input_string = str(input())
    list_line = list(input_string.split(" "))
    students.append(list_line)
"""
print(students)

# student_name = str(input())
student_name = 'Harsh'
print(student_name)

for student in students:
    print(student)
    if student[0] == student_name:
        print(float(student[1]))
        print(float(student[2]))
        print(float(student[3]))
        raiting = (float(student[1]) + \
                   float(student[2]) + \
                   float(student[3])) / 3
                   
print(raiting)
print('%0.2f' % raiting)
    