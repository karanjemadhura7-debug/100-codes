#40 bst is valid

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_bst(root, minimum=float("-inf"), maximum=float("inf")):
    if root is None:
        return True

    if not (minimum < root.data < maximum):
        return False

    return (
        is_bst(root.left, minimum, root.data)
        and is_bst(root.right, root.data, maximum)
    )


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

if is_bst(root):
    print("The tree is a valid BST")
else:
    print("The tree is not a valid BST")
