"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int:
    # Initialize the diameter
    diameter = [0]

    def height(node):
        if not node:
            return 0

        # Recursively find the height of left and right subtrees
        left_height = height(node.left)
        right_height = height(node.right)

        # Update the diameter if the path through this node is longer
        diameter[0] = max(diameter[0], left_height + right_height)

        # Return the height of this node
        return max(left_height, right_height) + 1

    height(root)
    return diameter[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameterOfBinaryTree(root))  # Output: 3 (the path is 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)
