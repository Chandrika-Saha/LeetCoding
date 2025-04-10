# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #--------------------- Recursive DFS ---------------------
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



        # #--------------------- Iterative DFS ------------------------
        # if not root:
        #     return 0
        # stack = [[root, 0]]
        # max_level = 0

        # while stack:
        #     node, level = stack.pop()
        #     max_level = max(max_level, level)

        #     if node:
        #         stack.append([node.left, level + 1])
        #         stack.append([node.right, level + 1])

        # return max_level



        # #-------------------- Iterative BFS -----------------------
        # if not root:
        #     return 0

        # level = 0
        # queue = deque([root])

        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     level += 1

        # return level

        