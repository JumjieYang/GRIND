class Solution:
    def two_sum(self, nums, target):
        visited = {}
        
        for i, num in enumerate(nums):
            if target - num in visited:
                return [visited[target - num], i]
            
            visited[num] = i
        