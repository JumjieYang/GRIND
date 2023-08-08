from collections import Counter


class Solution:
    def is_anagram(self, s, t):
        counter = Counter(s)

        for c in t:
            if c not in counter or counter[c] == 0:
                return False
            counter[c] -= 1

        for val in counter.values():
            if val != 0:
                return False

        return True
