from collections import defaultdict


class Solution:
    def group_anagrams(self, strs):
        group = defaultdict(list)

        for s in strs:
            cur = [0] * 26

            for c in s:
                cur[ord(c) - ord('a')] += 1

            group[tuple(cur)].append(s)

        return group.values()
