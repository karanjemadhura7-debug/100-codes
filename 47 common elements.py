47 common elements

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = list(set(list1) & set(list2))

print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common)
