class Solution:
    def majority_element(self, nums):
        majority = count = 0

        for num in nums:
            if count == 0:
                majority = num

            count += 1 if majority == num else -1

        return majority
