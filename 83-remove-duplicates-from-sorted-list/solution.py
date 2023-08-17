class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head):
        if not head or not head.next:
            return head

        dummy = cur = ListNode(-101, head)

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next

            cur = cur.next

        return dummy.next
