class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        res = []

        def preorder(node):
            if not node:
                res.append('x')
                return

            res.append(str(node.val))

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return ' '.join(res)

    def deserialize(self, data):

        def preorder(arr):
            val = next(arr)

            if not val or val == 'x':
                return

            node = TreeNode(val)
            node.left = preorder(arr)
            node.right = preorder(arr)

            return node

        return preorder(iter(data.split()))
