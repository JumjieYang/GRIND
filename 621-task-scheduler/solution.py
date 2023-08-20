import collections


class Solution:
    def least_interval(self, tasks, n):
        counter = collections.Counter(tasks)

        freqs = sorted(counter.values())

        max_freq = freqs.pop()

        idle_time = (max_freq - 1) * n

        while freqs:
            idle_time -= min(max_freq - 1, freqs.pop())

        return max(0, idle_time) + len(tasks)
