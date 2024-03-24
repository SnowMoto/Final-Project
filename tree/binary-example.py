class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        elif value > root.value:
            root.right = insert(root.right, value)
    return root

# Create a root node with value 10
root = TreeNode(10)

# Insert 7 into the binary tree
root = insert(root, 7)

# Comparing 7 with the root node's value where is it going?
if 7 < root.value:
    print("7 should be placed to the left of the root node.")
elif 7 > root.value:
    print("7 should be placed to the right of the root node.")
else:
    print("7 is equal to the root node's value.")

