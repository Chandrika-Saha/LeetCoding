"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}

        def dfs(node):

            if node in mapping:
                return mapping[node]
            
            copyNode = Node(node.val)
            mapping[node] = copyNode

            for neighbor in node.neighbors:
                clone = dfs(neighbor)
                copyNode.neighbors.append(clone)
            return copyNode

        return dfs(node) if node else None
        
