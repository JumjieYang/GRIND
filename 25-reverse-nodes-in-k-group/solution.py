class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        cur = head
        n = k

        while cur and n:
            cur = cur.next
            n -= 1

        if n > 0:
            return head

        new_head = self.reverse(head, k)

        head.next = self.reverseKGroup(cur, k)

        return new_head

    def reverse(self, node, k):
        prev = None
        cur = node

        for _ in range(k):
            nxt = cur.next

            cur.next = prev

            prev = cur
            cur = nxt
        return prev
