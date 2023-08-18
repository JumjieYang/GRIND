import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_bst(self, root):
        def helper(min_so_far, node, max_so_far):
            if not node:
                return True

            if not min_so_far < node.val < max_so_far:
                return False

            return helper(min_so_far, node.left, node.val) and helper(node.val, node.right, max_so_far)

        return helper(-math.inf, root, math.inf)
