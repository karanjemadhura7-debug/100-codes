#49 student marks dictionary

students = {
    "Aarav": 85,
    "Riya": 92,
    "Kabir": 78,
    "Ananya": 95
}

print("Student Marks:")

for name, marks in students.items():
    print(name, ":", marks)

highest_student = max(students, key=students.get)

print("Highest scorer:", highest_student)
print("Marks:", students[highest_student])
