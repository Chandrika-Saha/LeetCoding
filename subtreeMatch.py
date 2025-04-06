# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the subtree is null then it is a subtree of the other tree
        if not subRoot:
            return True
        # If the root is null then it cannot contain the subtree of the other tree 
        # unless the other tree is also not null
        if not root:
            return False

        # if the root and and subroot are the same tree, return True
        if self.same_tree(root, subRoot):
            return True
      
        # Otherwise, check both the left and right subtrees 
        # if either match, return True, otherwise False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def same_tree(self, s, t):
        # If both s and t are null, means that they match
        if not s and not t:
            return True
        # If s and t both nodes exists and their values match, check the other nodes of both tree
        # If all the nodes match, return True
        if s and t and s.val == t.val:
            return (self.same_tree(s.left, t.left) and
                self.same_tree(s.right, t.right))
        # The other case is when the values of s and t does not match,
        # either s is null and t is null
        # in all these cases, return False
        return False


        