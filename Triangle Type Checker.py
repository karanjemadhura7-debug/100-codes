# 26. Triangle Type Checker

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Sides must be positive.")
elif a + b <= c or b + c <= a or a + c <= b:
    print("Invalid triangle.")
elif a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
