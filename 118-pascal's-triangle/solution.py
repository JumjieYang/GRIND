class Solution:
    def generate(self, num_rows):
        res = []

        for i in range(num_rows):
            cur = [1] * (i + 1)

            for j in range(1, i):
                cur[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(cur)

        return res
