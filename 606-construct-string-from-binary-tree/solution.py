class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree_2_str(self, root):
        res = []

        def dfs(node):
            if not node:
                return

            res.append(str(node))
            if not node.left and not node.right:
                return

            res.append('(')
            dfs(node.left)
            res.append(')')

            if node.right:
                res.append('(')
                dfs(node.right)
                res.append(')')

        dfs(root)

        return ''.join(res)
