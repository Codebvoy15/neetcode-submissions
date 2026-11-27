# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 
        def Height(root):
            nonlocal diameter
            if root is None:
                return 0 

            leftHeight = Height(root.left)
            rightHeight  = Height(root.right)

            diameter = max(diameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)  # Return height to parent

        Height(root)                          # Start recursion from root

        return diameter