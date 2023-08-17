class ListNode:
    def __init__(self, x):
        self.val = x

        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self, homepage):
        self.head = ListNode(homepage)

        self.cur = self.head

    def visit(self, url):
        node = ListNode(url)

        self.cur.next = node
        node.prev = self.cur

        self.cur = self.cur.next

    def back(self, steps):
        while self.cur.prev and steps:
            self.cur = self.cur.prev
            steps -= 1

        return self.cur.val

    def forward(self, steps):
        while self.cur.next and steps:
            self.cur = self.cur.next

            steps -= 1

        return self.cur.val
