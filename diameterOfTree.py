# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        def dfs(root):
            if not root:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1

        all_diameters = []

        nodes = [root]
        while nodes:
            node = nodes.pop()
            dia = 0
            if node.left:
                nodes.append(node.left)
                dia += dfs(node.left)
            if node.right:
                nodes.append(node.right)
                dia += dfs(node.right)

            all_diameters.append(dia)

        # print(all_diameters)
        return max(all_diameters)