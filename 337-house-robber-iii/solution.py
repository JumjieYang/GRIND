class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root):
        if not root:
            return 0

        def dfs(node):
            if not node:
                return [0, 0]

            left, right = dfs(node.left), dfs(node.right)

            with_node = left[1] + right[1] + node.val
            without_node = max(left) + max(right)

            return [with_node, without_node]

        return max(dfs(root))
