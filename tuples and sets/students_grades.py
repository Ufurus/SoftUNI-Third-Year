number_of_students = int(input())
students = {}

for n in range(number_of_students):
    student, grade = input().split()

    if student not in students:
        students[student] = []
        students[student].append(float(grade))
    else:
        students[student].append(float(grade))

for stu,grad in students.items():
    average_grade = sum(grad) / len(grad)
    print(f"{stu} -> {' '.join([f'{el:.2f}' for el in grad])} (avg: {average_grade:.2f})")