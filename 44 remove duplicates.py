#44 remove duplicates

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = list(dict.fromkeys(numbers))

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)
