class Solution:
    def search_range(self, nums, target):
        def binary_search(nums, target, left_bias):
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    res = mid

                    if left_bias:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return res

        return [binary_search(nums, target, True), binary_search(nums, target, False)]
