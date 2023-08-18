import math
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def good_nodes(self, root):
        if not root:
            return None

        res = 0

        q = deque([(root, -math.inf)])

        while q:
            node, max_so_far = q.popleft()

            if node.val >= max_so_far:
                res += 1
                max_so_far = node.val

            for child in (node.left, node.right):
                if child:
                    q.append((child, max_so_far))

        return res
