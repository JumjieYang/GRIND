import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        if val in self.dict:
            return False

        self.dict[val] = len(self.list)

        self.list.append(val)

        return True

    def remove(self, val):
        if val not in self.dict:
            return False

        last_element = self.list[-1]

        idx = self.dict[val]

        self.list[idx] = last_element

        self.dict[last_element] = idx

        self.dict.pop(val)

        self.list.pop()

        return True

    def getRandom(self):
        idx = random.randint(0, len(self.list) - 1)

        return self.list[idx]
