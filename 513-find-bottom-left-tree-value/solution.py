from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_bottom_left_value(self, root):
        if not root:
            return 0

        res = (0, -1)

        q = deque([(root, 0), ])

        while q:
            node, level = q.popleft()

            if level > res[1]:
                res = (node.val, level)

            level += 1

            for child in (node.left, node.right):
                if child:
                    q.append((child, level))

        return res[0]
