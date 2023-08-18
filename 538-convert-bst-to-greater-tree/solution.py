class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convert_bst(self, root):
        sums = 0
        if not root:
            return None

        def inorder(node):
            if not node:
                return 0

            inorder(node.right)

            nonlocal sums

            sums += node.val

            node.val = sums

            inorder(node.left)

            return node

        return inorder(root)
