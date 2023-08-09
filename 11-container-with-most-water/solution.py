class Solution:
    def max_area(self, height):
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            width = r - l
            if height[l] < height[r]:
                res = max(res, height[l] * width)
                l += 1
            else:
                res = max(res, height[r] * width)

                r -= 1

        return res
