#34 bst min max

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def find_min(root):
    while root.left:
        root = root.left
    return root.data


def find_max(root):
    while root.right:
        root = root.right
    return root.data


root = None

for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)

print("Minimum value:", find_min(root))
print("Maximum value:", find_max(root))
