class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return root

        cur, nxt = root, root.left

        while cur and nxt:
            cur.left.next = cur.right

            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next

            if not cur:
                cur = nxt
                nxt = cur.left

        return root
