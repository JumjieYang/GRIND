from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum_numbers(self, root):
        if not root:
            return 0

        res = 0

        q = deque([(root, 0)])

        while q:
            node, cur = q.popleft()

            cur = cur * 10 + node.val

            if not node.left and not node.right:
                res += cur
                continue

            for child in (node.left, node.right):
                if child:
                    q.append((child, cur))

        return res
