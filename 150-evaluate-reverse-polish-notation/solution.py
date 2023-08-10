class Solution:
    def eval_rpn(self, tokens):
        stack = []

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }

        for t in tokens:
            if t in ops:
                op = ops[t]

                num2, num1 = stack.pop(), stack.pop()

                t = op(num1, num2)
            stack.append(int(t))

        return sum(stack)
