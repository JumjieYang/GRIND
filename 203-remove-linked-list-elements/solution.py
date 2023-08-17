class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_elements(self, head, val):
        dummy = cur = ListNode()
        dummy.next = head

        while cur:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next

            cur = cur.next

        return dummy.next
