class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def all_possible_fbt(self, n):
        dp = {0: [], 1: [TreeNode()]}

        def dfs(n):
            if n in dp:
                return dp[n]

            res = []

            for l in range(n):
                r = n - 1 - l

                left_subs, right_subs = dfs(l), dfs(r)

                for left in left_subs:
                    for right in right_subs:
                        root = TreeNode(0, left, right)

                        res.append(root)

            dp[n] = res

            return res

        return dfs(n)
