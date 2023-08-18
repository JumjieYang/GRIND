from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def width_of_binary_tree(self, root):
        if not root:
            return 0

        res = 0

        q = deque([(root, 0)])

        while q:
            left = q[0][1]
            right = 0

            for _ in range(len(q)):
                node, cur = q.popleft()

                right = cur

                if node.left:
                    q.append((node.left, 2 * cur))

                if node.right:
                    q.append((node.right, 2 * cur + 1))

            res = max(res, right - left + 1)

        return res
