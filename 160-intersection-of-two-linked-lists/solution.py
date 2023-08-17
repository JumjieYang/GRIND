class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_intersection_node(self, headA, headB):
        cur_a, cur_b = headA, headB

        while cur_a != cur_b:
            cur_a = headB if not cur_a else cur_a.next
            cur_b = headA if not cur_b else cur_b.next

        return cur_a
