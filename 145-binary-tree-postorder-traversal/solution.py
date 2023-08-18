class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def postorder_traversal(self, root):
        res = []

        def postorder(node):
            if not node:
                return

            postorder(node.left)
            postorder(node.right)

            res.append(node.val)

        postorder(root)

        return res
