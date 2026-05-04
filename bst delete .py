class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Insert
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# Find Inorder Successor
def min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


# Delete Node
def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)

    elif key > root.key:
        root.right = delete(root.right, key)

    else:
        # Case 1: No child / Leaf node
        if root.left is None and root.right is None:
            return None

        # Case 2: One child in either left or right
        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        # Case 3: Two children
        temp = min_value(root.right)   # inorder successor
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    return root


# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Main code
root = None
values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    root = insert(root, v)

print("Before Deletion:")
inorder(root)

root = delete(root, 50)   # deleting node with two children

print("\nAfter Deletion:")
inorder(root)