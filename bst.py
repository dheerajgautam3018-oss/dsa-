class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Insert in BST 
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# Search in BST
def search(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)

    return search(root.right)


# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Main
root = None
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

print("Inorder Traversal:")
inorder(root)

result = search(root, 40)

if result:
    print("\nElement Found")
else:
    print("\nElement Not Found")