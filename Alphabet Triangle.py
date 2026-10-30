# 30. Alphabet Triangle

n = int(input("Enter the number of rows (1-26): "))

if n < 1 or n > 26:
    print("Please enter a number between 1 and 26.")
else:
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()
