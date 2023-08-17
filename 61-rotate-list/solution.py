class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotate_right(self, head, k):
        if not head or not head.next:
            return head

        cur = head
        n = 1

        while cur.next:
            cur = cur.next
            n += 1

        cur.next = head
        k %= n

        cur = head

        for _ in range(n - k - 1):
            cur = cur.next

        res = cur.next

        cur.next = None

        return res
