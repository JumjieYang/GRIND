class Solution:
    def merge(self, nums1, m, nums2, n):
        i, j = m - 1, n - 1

        for p in range(m + n - 1, -1, -1):
            if j < 0:
                break

            if i > -1 and nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
