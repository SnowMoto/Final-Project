# Tree Data Structure

**What is a Tree Data Structure and how does it work?**

Tree Data Structure is an organized system to store data. Similar to your computer file system. There is a root like folder for your pictures or in the image to see a visual, which is "P". From there other folders or nodes are organized data branches from that root. In your picture folder there are folders labeled "Vacation", "Wedding", "Baby Birth" and etc. Each folder will have image data or nodes that are associated.

![Tree Map](tree_map.png)

As you look at the image lets go over each part that is labeled. 
* Root - starting point of the tree and also known as the "Key".
* Edge - the connection to the next node.
* Parent - a node that has other node branches known as children.
* Subtree - is used when the tree becomes very large and need to new starting point.
* Height - the number of nodes under the root. In the image it has 4.

**What does this look like in Python?**
In Python there are two Tree types:
1. Binary Tree
2. Balancing Tree

# Binary Tree

A tree where each node has at most two nodes to have one for left and one go right. This image below has its numbers organized where the left is smaller numbers and the right will have larger numbers.

![Binary Tree](binary-tree.png)

When entering data into a tree, let’s say you are entering a number 7 you will need to use a comparison method of that value to the root. Then have the method decide if the value 7 is placed left or right in the tree. Click on the link below for an example.

[Binary Example](binary-example.py)

# Balancing Tree

This is to test if the Binary Tree is balanced based on the height using Big-O-notation learned in stacks: O(log n) to compare if they are not more than 1. It also will check to see if the subtrees are balanced. 

* Reference Link: [GeeksforGeeks - Balanced Tree](https://www.geeksforgeeks.org/balanced-binary-tree/)

[Balancing Tree](balanced.png)

Here is an example of Python code to test to see if a Binary Tree is balanced or unbalanced. If it is unbalanced this would need to be fixed. 

[Balanced or Unbalanced Example](balanced.py)

**Important code to know and understand to utilize this structure as follows:**

***insert(value)***
Add value to the tree with using O(Log n) for every new node that is being added the tree gets smaller and smaller to execute recursively.

`insert(value)`

***remove(value)***
Delete values from the tree and is a Log(n) to apply recursion.

`remove(value)`

***traverse***
It is to check for every node in the tree. This can go from smallest to greatest or reverse. This will use O(n) as it only needs to go through the tree once.

***height(node)***
Returns the height of the entire tree from the root to the last node. To do this you would use O(n) as it only needs to check one time.

`height(value)`

***size***
Return the size of the BST (Binary Search Tree). It is implemented to track the size of the tree and or to make sure it is empty.

`size()`

**Ready for Examples?**

Ok lets got back over briefly what you have learned:
1. Tree Data Structure is organized data that has a root it branches from.
2. There are two types of Trees:
* Binary - each parent node has at most two nodes. 
* Balancing - method to check if the tree is balanced for efficient python programming.
3. The parts of the Python code to implement:
    - insert - to add a nodes to the tree.
    - remove - to delete nodes from the tree.
    - traverse - check for every node in the tree.
    - height - returns the height of the tree starting at the root.
    - size - returns the BST of the tree. Empty or not!

***Challenge***

Now it is time to see if you can practice what you have learned. The could will be kept simple and not check for balances and etc. Do not be afraid to play around with your code to experiment.

[Circle of Life](circle_of_life.py)

[Solution](circle_solution.py)

