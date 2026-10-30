# 28. Pascal's Triangle

n = int(input("Enter the number of rows: "))

for i in range(n):

    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")

    num = 1

    for j in range(i + 1):
        print(num, end=" ")

        # Calculate the next number in the row
        num = num * (i - j) // (j + 1)

    print()
