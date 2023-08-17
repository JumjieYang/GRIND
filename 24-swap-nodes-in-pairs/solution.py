class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solution:
    def swap_pairs(self, head):
        if not head or not head.next:
            return head

        dummy = prev = ListNode()

        while head and head.next:
            cur, nxt = head, head.next

            prev.next = nxt
            cur.next = nxt.next
            nxt.next = cur

            prev = cur

            head = head.next

        return dummy.next
