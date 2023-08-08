class Solution:
    def find_difference(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        res1, res2 = [], []

        for num in nums1:
            if num not in nums2:
                res1.append(num)

        for num in nums2:
            if num not in nums1:
                res2.append(num)

        return [res1, res2]
