

students = [('Squidward', 'B', 60),
            ('Patrick', 'D', 42),
            ('Spongebob', 'A', 25),
            ('Sandy', 'E', 26),
            ('Mr. Krabs', 'F', 80)]


def grade(grades): return grades[1]


students.sort(key=grade)

for i in students:
    print(i)
