# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # If the first node is null, empty tree, return True
        if not root:
            return True
        
        # Set flag to False, this is a global variable to keep track of balanceness of the tree
        flag = False

        # Recursive method, dfs
        def depth(root):

            # Declare flag as nonlocal so that it modifies the global variable
            nonlocal flag

            # If the root is empty
            if not root:
                # Return True for the leaf nodes
                return [True, 0]
            # Get the left and right subtree's height
            left, right = depth(root.left), depth(root.right)
            # Update the flag based on all the heights seen so far
            flag = True if abs(left[1] - right[1]) <= 1 and left[0] and right[0] else False

            # Return the updated flag, starting from the leaf node and the height 
            return [flag, 1 + max(left[1], right[1])]

        # Call the recursive dfs
        depth(root)

        return flag # Return the global variable flag
