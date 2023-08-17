class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head):
        if not head or not head.next:
            return head

        prev, cur = None, head

        while cur:
            nxt = cur.next

            cur.next = prev

            prev = cur
            cur = nxt

        return prev
