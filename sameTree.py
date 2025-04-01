# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # First base case, if both nodes are empty, they are the same, return true
        if not p and not q:
            return True

        # If one of them is empty, other one is not: they do not match, return False
        # Also, if there values does not match, return False
        if not p or not q or p.val != q.val:
            return False
       
        # If both the subtrees return True, only then they are the same tree
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        