class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_to_bst(self, nums):
        def helper(l, r):
            if l > r:
                return

            mid = (l + r) // 2

            return TreeNode(nums[mid], helper(l, mid - 1), helper(mid + 1, r))

        return helper(0, len(nums) - 1)
