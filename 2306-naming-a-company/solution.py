from collections import defaultdict


class Solution:
    def distinct_names(self, ideas):
        group = defaultdict(set)

        for idea in ideas:
            group[idea[0]].add(idea[1:])

        keys = list(group.keys())

        res = 0

        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                group1 = group[keys[i]]
                group2 = group[keys[j]]

                intersection = group1.intersection(group2)

                res += 2 * (len(group1) - len(intersection)) * (len(group2) - len(intersection))

        return res
