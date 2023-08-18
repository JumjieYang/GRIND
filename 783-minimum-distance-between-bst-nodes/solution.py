import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_diff_in_bst(self, root):
        prev = None
        diff = math.inf

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            nonlocal prev, diff

            if prev:
                diff = min(diff, node.val - prev.val)

            prev = node

            dfs(node.right)

        dfs(root)

        return diff
