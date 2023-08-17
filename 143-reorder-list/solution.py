class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorder_list(self, head):
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
            return head

        tail = reverse(get_mid(head))

        dummy = cur = ListNode()

        from_head = True

        while head and tail:
            if from_head:
                cur.next = head
                head = head.next
            else:
                cur.next = tail
                tail = tail.next
            from_head = not from_head
            cur = cur.next

        return dummy.next
