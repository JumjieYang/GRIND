class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sort_list(self, head):
        if not head or not head.next:
            return head

        def get_mid(node):
            slow, fast = None, node

            while fast and fast.next:
                slow = slow.next if slow else fast
                fast = fast.next.next

            res = slow.next

            slow.next = None

            return res

        def merge(l1, l2):
            dummy = cur = ListNode()

            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next

                cur = cur.next

            if l1:
                cur.next = l1
            if l2:
                cur.next = l2

            return dummy.next

        def divide(node):
            if not node or not node.next:
                return node

            mid = get_mid(node)

            left, right = divide(node), divide(mid)

            return merge(left, right)

        return divide(head)
