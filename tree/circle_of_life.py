class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_character(parent, side, data):
    """Create a function that inserts the characters into the tree.
    """
    
    pass

def preorder_traversal(node):
    """Create a function to use traverse to order characters based on their relationship.
    Hint: The King is always first and followed by who? Scar is not next in the Kings line.
    """
    
    pass

# Creating characters from the Lion King movie
mufasa = TreeNode("Mufasa")
simba = TreeNode("Simba")
scar = TreeNode("Scar")
nala = TreeNode("Nala")
timon = TreeNode("Timon")
zazu = TreeNode("Zazu")
rafiki = TreeNode("Rafiki")

# The relationships between characters
mufasa.left = simba
mufasa.right = scar
simba.left = nala
simba.right = timon
scar.left = zazu
scar.right = rafiki

# Preorder traversal to print the characters
print("Preorder Traversal:")
preorder_traversal(mufasa)
