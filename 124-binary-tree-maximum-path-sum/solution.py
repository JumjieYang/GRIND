import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_path_sum(self, root):
        max_sum = -math.inf

        def helper(node):
            if not node:
                return 0

            left, right = max(helper(node.left), 0), max(helper(node.right), 0)

            nonlocal max_sum

            max_sum = max(max_sum, left + right + node.val)

            return node.val + max(left, right)

        helper(root)

        return max_sum
