from collections import Counter, defaultdict


class FreqStack:
    def __init__(self):
        self.freqs = Counter()
        self.max_freq = 0
        self.groups = defaultdict(list)

    def push(self, val):
        self.freqs[val] += 1

        self.max_freq = max(self.max_freq, self.freqs[val])

        self.groups[self.freqs[val]].append(val)

    def pop(self):
        val = self.groups[self.max_freq].pop()

        if len(self.groups[self.max_freq]) == 0:
            self.max_freq -= 1

        self.freqs[val] -= 1

        return val
