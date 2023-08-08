from collections import Counter


class Solution:
    def check_sumarray_sum(self, nums, k):
        counter = Counter()
        counter[0] = -1

        cur = 0

        for i, num in enumerate(nums):
            cur += num

            if cur % k in counter:
                if i - counter[cur % k] > 1:
                    return True

                continue

            counter[cur % k] = i

        return -1
