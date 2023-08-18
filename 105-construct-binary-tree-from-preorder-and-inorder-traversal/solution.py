class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bulid_tree(self, preorder, inorder):
        idx_map = {v: i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return

            val = preorder.pop(0)

            idx = idx_map[val]

            return TreeNode(val, helper(l, idx - 1), helper(idx + 1, r))

        return helper(0, len(inorder) - 1)
