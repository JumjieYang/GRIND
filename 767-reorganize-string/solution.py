import collections


class Solution:
    def reorganize_string(self, s):
        counter = collections.Counter()
        max_freq, char = 0, ''

        for c in s:
            counter[c] += 1

            if counter[c] > max_freq:
                max_freq = counter[c]
                char = c

        n = len(s)
        if max_freq > (n + 1) // 2:
            return ''

        cur = 0

        res = [''] * n
        for _ in range(counter.pop(char)):
            res[cur] = char
            cur += 2

        for char, count in counter.items():
            for _ in range(count):
                if cur >= n:
                    cur = 1

                res[cur] = char
                cur += 2

        return ''.join(res)
