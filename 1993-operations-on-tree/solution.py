from collections import deque


class LockingTree:
    def __init__(self, parent):
        self.parent = parent
        self.locked = [None] * len(parent)

        self.children = {i: [] for i in range(len(parent))}

        for i in range(1, len(parent)):
            self.children[parent[i]].append(i)

    def lock(self, num, user):
        if self.locked[num]:
            return False

        self.locked[num] = user

        return True

    def unlock(self, num, user):
        if self.locked[num] != user:
            return False

        self.locked[num] = None

        return True

    def upgrade(self, num, user):
        i = num

        while i != -1:
            if self.locked[i]:
                return False

            i = self.parent[i]

        locked_count, q = 0, deque([num])

        while q:
            node = q.popleft()

            for child in self.children[node]:
                if self.locked[child]:
                    self.locked[child] = None
                    locked_count += 1

                q.append(child)

        if locked_count == 0:
            return False

        self.locked[num] = user

        return True
