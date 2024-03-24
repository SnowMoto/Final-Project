class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_character(parent, side, data):
    """Create a function that inserts the characters into the tree.
    """
    
    if side == 'left':
        parent.left = TreeNode(data)
    elif side == 'right':
        parent.right = TreeNode(data)
    else:
        print("Invalid side. Use 'left' or 'right'.")

def preorder_traversal(node):
    """Create a function to use traverse to order characters based on their relationship.
    Hint: The King is always first and followed by who? Scar is not next in the Kings line.
    """
    
    if node:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Characters for the Lion King movie
mufasa = TreeNode("Mufasa")
simba = TreeNode("Simba")
scar = TreeNode("Scar")
nala = TreeNode("Nala")
timon = TreeNode("Timon")
zazu = TreeNode("Zazu")
rafiki = TreeNode("Rafiki")

# Building the relationships between characters
mufasa.left = simba
mufasa.right = scar
simba.left = nala
simba.right = timon
scar.left = zazu
scar.right = rafiki

#Print Characters in the required traverse order.
print("Preorder Traversal:")
preorder_traversal(mufasa)
