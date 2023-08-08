class Solution:
    def next_greater_element(self, nums1, nums2):
        idx_map = {num: i for i, num in enumerate(nums1)}

        res = [-1] * len(nums1)

        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                val = stack.pop()

                idx = idx_map[val]

                res[idx] = num

            if num in idx_map:
                stack.append(num)

        return res
