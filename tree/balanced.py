class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def is_balanced(root):
    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    
    return False

# Example usage
# Constructing a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

# Comment out this row 31 to test for unbalanced.
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.left.left.left = TreeNode(7)

if is_balanced(root):
    print("The binary tree is balanced.")
else:
    print("The binary tree is not balanced.")
