class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
