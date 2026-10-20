# 14. Student Grade Calculator

marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks. Enter marks between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 40:
    print("Grade: E")
else:
    print("Grade: F (Fail)")
