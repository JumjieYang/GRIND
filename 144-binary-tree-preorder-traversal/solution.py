class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_traversal(self, root):
        res = []

        def preorder(node):
            if not node:
                return

            res.append(node.val)

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return res
