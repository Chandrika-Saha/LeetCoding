# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize result to track the maximum diameter
        res = 0
        
        def dfs(root):
            # Make res non-local so that it refers to the res declared outside the scope
            nonlocal res

            # If the root is None, it refers to a node with a zero height
            if not root:
                return 0

            # Left and right recursively contains the height of left and right subtrees
            # starting from the edge node, it keeps the maximum of res and the current diameter
            # In the end of all the recursive calls, res will have the diameter
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left+right)

            return 1 + max(left, right) # Consider the current node, add 1

        dfs(root)

        return res

        

        