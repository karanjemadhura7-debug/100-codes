#8. Largest of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number =", a)
elif b > a:
    print("Largest number =", b)
else:
    print("Both numbers are equal.")
