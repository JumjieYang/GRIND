class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(self, inorder, postorder):
        idx_map = {v: i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return

            val = postorder.pop()

            idx = idx_map[val]

            node = TreeNode(val)

            node.right = helper(idx + 1, r)
            node.left = helper(l, idx - 1)

            return node

        return helper(0, len(inorder) - 1)
