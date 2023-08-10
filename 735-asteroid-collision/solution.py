class Solution:
    def asteroid_collision(self, asteroids):
        stack = []

        for a in asteroids:
            push = True

            while push and stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                else:
                    if stack[-1] == -a:
                        stack.pop()

                    push = False

            if push:
                stack.append(a)

        return stack
