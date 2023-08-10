class Solution:
    def car_fleet(self, target, position, speed):
        pairs = [(position[i], speed[i]) for i in range(len(speed))]

        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            time = (target - p) / s

            if stack and stack[-1] >= time:
                continue

            stack.append(time)

        return len(stack)
