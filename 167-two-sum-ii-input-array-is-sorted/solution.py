class Solution:
    def two_sum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            sums = numbers[l] + numbers[r]

            if sums == target:
                return [l + 1, r + 1]
            elif sums < target:
                l += 1
            else:
                r -= 1

        return None
