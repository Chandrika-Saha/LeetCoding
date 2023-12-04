# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = collections.deque() 
        queue.append(root)
        result = []

        while queue:
            level = []
            queueLength = len(queue)

            for i in range(queueLength):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    print(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                result.append(level)
        
        return result
                
            


