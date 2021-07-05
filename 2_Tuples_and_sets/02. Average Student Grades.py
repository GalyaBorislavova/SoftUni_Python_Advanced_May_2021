def input_to_list(count):
    lines = []
    for _ in range(count):
        line = input()
        lines.append(line)
    return lines


def average(nums):
    return sum(nums) / len(nums)


n = int(input())
input_students_grades = input_to_list(n)
students_grades = {}

for student_data in input_students_grades:
    student_data = student_data.split(" ")
    student = student_data[0]
    grade = float(student_data[1])
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(grade)

for (student, grades) in students_grades.items():
    avg = average(grades)
    grades = [f"{g:.2f}" for g in grades]
    print(f"{student} -> {' '.join(grades)} (avg: {avg:.2f})")