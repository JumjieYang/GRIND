from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_duplicate_subtrees(self, root):
        pattern_to_id = {}

        counter = Counter()

        res = []

        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            pattern = (left, node.val, right)

            if pattern not in pattern_to_id:
                pattern_to_id[pattern] = len(pattern_to_id) + 1

            id = pattern_to_id[pattern]

            counter[id] += 1
            if counter[id] == 2:
                res.append(node)

            return id

        dfs(root)

        return res
