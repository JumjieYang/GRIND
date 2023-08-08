class Solution:
    def sort_array(self, nums):
        def merge(left, right):
            m, n = len(left), len(right)

            if m == 0:
                return right

            if n == 0:
                return left

            res = []

            i = j = 0

            while i < m and j < n:
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            while i < m:
                res.append(left[i])
                i += 1

            while j < n:
                res.append(right[j])
                j += 1

            return res

        def merge_sort(l, r):
            if l == r:
                return [nums[l]]

            if l > r:
                return []

            mid = (l + r) // 2

            left, right = merge_sort(l, mid), merge_sort(mid + 1, r)

            return merge(left, right)

        return merge_sort(0, len(nums) - 1)
