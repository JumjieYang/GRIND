class Solution:
    def minimize_max(self, nums, p):
        nums.sort()
        
        l, r = 0, nums[-1] - nums[0]
        
        def is_valid(diff):
            i, count = 0, 0
            
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= diff:
                    count += 1
                    i += 1
                
                i += 1
            
            return count >= p
        
        while l <= r:
            mid = (l + r) // 2
            
            if is_valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return r + 1