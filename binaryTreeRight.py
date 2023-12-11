# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return None

        treeNodes = collections.deque([root])
        allRights = []

        while treeNodes:

            rightSide = None
            length = len(treeNodes)

            for i in range(length):

                node = treeNodes.popleft()
                if node:
                    rightSide = node
                    treeNodes.append(node.left)
                    treeNodes.append(node.right)
                
            if rightSide:
                allRights.append(rightSide.val)

        return allRights




