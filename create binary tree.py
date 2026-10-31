#31 create binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)

print("Root:", root.data)
print("Left child:", root.left.data)
print("Right child:", root.right.data)
