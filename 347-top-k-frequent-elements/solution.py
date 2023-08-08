import random
from collections import Counter


class Solution:
    def top_k_frequent(self, nums, k):
        freqs = Counter(nums)

        nums = list(freqs.keys())

        def partition(l, r):
            idx = random.randint(l, r)

            pivot = freqs[nums[idx]]

            nums[idx], nums[r] = nums[r], nums[idx]

            for i in range(l, r):
                cur = freqs[nums[i]]

                if cur >= pivot:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1

            nums[l], nums[r] = nums[r], nums[l]

            return l

        l, r = 0, len(nums) - 1

        while l < r:
            pivot = partition(l, r)

            if pivot == k:
                break
            elif pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1

        return nums[:k]
