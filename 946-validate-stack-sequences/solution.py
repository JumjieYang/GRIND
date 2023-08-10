class Solution:
    def validate_stack_sequences(self, pushed, popped):
        stack = []
        i = 0

        for n in pushed:
            stack.append(n)

            while stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1

        return len(stack) == 0
