class Solution:
    def contains_nearby_duplicate(self, nums, k):
        visited = set()

        for i, num in enumerate(nums):
            if num in visited:
                return True

            visited.add(num)

            if len(visited) > k:
                visited.remove(nums[i - k])

        return False
