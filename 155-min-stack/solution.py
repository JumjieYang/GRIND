class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if len(self.stack) == 0 or val < self.getMin():
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.getMin()))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
