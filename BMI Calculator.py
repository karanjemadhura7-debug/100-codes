# 17. BMI Calculator

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

if weight <= 0 or height <= 0:
    print("Weight and height must be positive.")
else:
    bmi = weight / (height ** 2)

    print("Your BMI =", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obesity")
