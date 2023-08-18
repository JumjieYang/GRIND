class Solution:
    def diameter_of_binary_tree(self, root):
        if not root:
            return 0

        diameter = 0

        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            nonlocal diameter

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)

        return diameter
