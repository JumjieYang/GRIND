class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pair_sum(self, head):
        if not head or not head.next:
            return 0

        def get_mid(node):
            slow = fast = node

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def reverse(node):
            prev, cur = None, node

            while cur:
                nxt = cur.next

                cur.next = prev
                prev = cur
                cur = nxt

            return prev

        tail = reverse(get_mid(head))

        res = 0

        while tail:
            res = max(res, tail.val + head.val)

            head = head.next
            tail = tail.next

        return res
