class Solution:
    def contains_duplicate(self, nums):
        visited = set()

        for num in nums:
            if num in visited:
                return True

            visited.add(num)

        return False
