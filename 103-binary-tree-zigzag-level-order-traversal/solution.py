from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzag_level_order(self, root):
        if not root:
            return []

        res = []

        q = deque([root, ])
        level = 0
        while q:
            cur = []

            for _ in range(len(q)):
                node = q.popleft()

                if level % 2:
                    cur.insert(0, node.val)
                else:
                    cur.append(node.val)

                for child in (node.left, node.right):
                    if child:
                        q.append(child)

            res.append(cur)
            level += 1

        return res
