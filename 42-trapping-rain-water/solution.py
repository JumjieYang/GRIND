class Solution:
    def trap(self, height):
        l, r = 0, len(height) - 1

        max_l, max_r = 0, 0
        res = 0
        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])

            if height[l] < height[r]:
                res += max_l - height[l]
                l += 1
            else:
                res += max_r - height[r]
                r -= 1

        return res
