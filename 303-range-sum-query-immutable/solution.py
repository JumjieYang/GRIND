class NumArray:

    def __init__(self, nums):
        prefix_sums = []

        cur = 0

        for num in nums:
            prefix_sums.append(cur)

            cur += num

        prefix_sums.append(cur)

        self.sums = prefix_sums

    def sumRange(self, left, right):
        return self.sums[right + 1] - self.sums[left]
