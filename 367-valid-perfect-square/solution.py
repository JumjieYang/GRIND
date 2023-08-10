class Solution:
    def is_perfect_square(self, num):
        l, r = 1, num

        while l <= r:
            mid = (l + r) // 2

            res = mid ** 2

            if res == num:
                return True
            elif res < num:
                l = mid + 1
            else:
                r = mid - 1

        return False
