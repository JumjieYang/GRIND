from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_complete_tree(self, root):
        if not root:
            return True

        null_flag = False

        q = deque([root, ])

        while q:
            node = q.popleft()

            if not node:
                null_flag = True
            else:
                if null_flag:
                    return False

                for child in (node.left, node.right):
                    q.append(child)

        return True
