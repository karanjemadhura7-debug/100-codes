#45 second largest number

numbers = [10, 25, 45, 32, 45, 8]

unique_numbers = sorted(set(numbers), reverse=True)

if len(unique_numbers) >= 2:
    second_largest = unique_numbers[1]
    print("Second-largest number:", second_largest)
else:
    print("Second-largest number does not exist")
