
students = [100, 90, 85, 70, 40, 30, 25, 0]

# passed_students = list(filter(lambda x: x >= 60, students))

# passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else 'FAILED' for i in students]
print(passed_students)
