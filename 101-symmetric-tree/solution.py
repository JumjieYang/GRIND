class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root):
        def is_same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            return p.val == q.val and is_same_tree(p.left, q.right) and is_same_tree(p.right, q.left)

        return is_same_tree(root, root)
