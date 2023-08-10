import math


class Solution:
    def find_median_sorted_arrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)

        if m > n:
            return self.find_median_sorted_arrays(nums2, nums1)

        l, r = 0, m

        while l < r:
            mid = (l + r) // 2
            mid2 = (m + n + 1) // 2 - mid

            max_l_1 = -math.inf if mid == 0 else nums1[mid - 1]
            max_l_2 = -math.inf if mid2 == 0 else nums2[mid2 - 1]
            min_r_1 = math.inf if mid == m else nums1[mid]
            min_r_2 = math.inf if mid2 == n else nums2[mid2]

            if max_l_1 <= min_r_2 and max_l_2 <= min_r_1:
                if (m + n) % 2 == 1:
                    return max(max_l_1, max_l_2)

                return (max(max_l_1, max_l_2) + min(min_r_1, min_r_2)) / 2.0

            elif max_l_1 >= min_r_2:
                r = mid - 1
            else:
                l = mid + 1

        return -1
