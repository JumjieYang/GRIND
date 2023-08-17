class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):
        dummy_small = p_s = ListNode()

        dummy_large = p_l = ListNode()

        while head:
            if head.val < x:
                p_s.next = head

                p_s = p_s.next
            else:
                p_l.next = head

                p_l = p_l.next

            head = head.next

        p_l.next = None

        p_s.next = dummy_large.next

        return dummy_small.next
