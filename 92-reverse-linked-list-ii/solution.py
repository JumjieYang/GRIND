class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_between(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(-501, head)

        left_prev, cur = dummy, head

        for _ in range(left - 1):
            left_prev = cur
            cur = cur.next

        prev = None

        for _ in range(right - left + 1):
            nxt = cur.next

            cur.next = prev

            prev = cur
            cur = nxt

        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next
