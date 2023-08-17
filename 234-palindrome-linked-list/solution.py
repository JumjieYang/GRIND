class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome(self, head):
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

        if not head or not head.next:
            return True

        tail = reverse(get_mid(head))

        while tail:
            if head.val != tail.val:
                return False

            head = head.next
            tail = tail.next

        return True
