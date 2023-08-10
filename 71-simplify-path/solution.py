class Solution:
    def simplify_path(self, path):
        stack = []

        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()

            elif p == '.' or p == '':
                continue
            else:
                stack.append(p)

        return '/' + '/'.join(stack)
