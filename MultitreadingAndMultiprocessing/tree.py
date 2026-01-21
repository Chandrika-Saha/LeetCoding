class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST: # Binary Search Tree
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            # Root is empty
            if not node:
                return TreeNode(val)
            #
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node

        self.root = _insert(self.root, val)

    def search(self, val):
        cur = self.root
        while cur:
            if cur.val == val:
                return True
            cur = cur.left if val < cur.val else cur.right
        return False

    # Traversals
    def inorder(self):
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(self.root)
        return res

    def preorder(self):
        res = []
        def dfs(node): # Depth First Search
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(self.root)
        return res

    def postorder(self):
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(self.root)
        return res


