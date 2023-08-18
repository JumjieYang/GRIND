class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key):
        def succ(node):
            node = node.right

            while node.left:
                node = node.left

            return node.val

        def pred(node):
            node = node.left

            while node.right:
                node = node.right

            return node.val

        if not root:
            return

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return

            if root.left:
                root.val = pred(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = succ(root)
                root.right = self.deleteNode(root.right, root.val)

        return root
