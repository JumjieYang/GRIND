class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root):
        res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            res.append(node.val)

            inorder(node.right)

        inorder(root)

        return res
