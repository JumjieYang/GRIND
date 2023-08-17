class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(self, lists):
        if not lists:
            return None

        idx = 1

        n = len(lists)

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

        while idx < n:
            for i in range(0, n - idx, idx * 2):
                lists[i] = merge(lists[i], lists[i + idx])

            idx *= 2

        return lists[0]
