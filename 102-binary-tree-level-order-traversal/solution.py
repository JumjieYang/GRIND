from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root):
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            cur = []

            for _ in range(len(q)):
                node = q.popleft()

                cur.append(node.val)

                for child in (node.left, node.right):
                    if child:
                        q.append(child)

            res.append(cur)

        return res
