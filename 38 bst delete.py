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
    return root


#38 bst delete

def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        successor = find_min(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = None

for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)

root = delete(root, 30)

print("BST after deleting 30:")
inorder(root)
