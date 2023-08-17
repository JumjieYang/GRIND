class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copy_random_list(self, head):
        copy = {}

        def dfs(node):
            if not node:
                return None

            if node in copy:
                return copy[node]

            copy[node] = Node(node.val)

            copy[node].next = dfs(node.next)
            copy[node].random = dfs(node.random)

            return copy[node]

        return dfs(head)
