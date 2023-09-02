class Solution:
    def can_partition_k_subsets(self, nums, k):
        sums = sum(nums)
        
        if sums % k != 0:
            return False
        
        target = sums // k
        
        nums.sort(reverse=True)
        
        used = [False] * len(nums)
        
        def dfs(i, k, cur_sum):
            if k == 0:
                return True
            
            if cur_sum == target:
                return dfs(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if j > 0 and not used[j - 1] and nums[j] == nums[j - 1]:
                    continue
                
                if used[j] or cur_sum + nums[j] > target:
                    continue
                
                used[j] = True
                
                if dfs(j + 1, k, cur_sum + nums[j]):
                    return True
                
                used[j] = False
            
            return False
        
        return dfs(0, k, 0)