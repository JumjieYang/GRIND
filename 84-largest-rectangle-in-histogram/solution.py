class Solution:
    def largest_rectangle_area(self, heights):
        stack = [-1]
        n = len(heights)
        res = 0
        for i in range(n):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1

                res = max(res, cur_height * cur_width)

            stack.append(i)

        while stack[-1] != -1:
            cur_height = heights[stack.pop()]
            cur_width = n - stack[-1] - 1

            res = max(res, cur_height * cur_width)

        return res
