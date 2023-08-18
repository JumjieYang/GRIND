class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root):

        def helper(node):
            if not node:
                return 0

            left, right = helper(node.left), helper(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return helper(root) != -1
