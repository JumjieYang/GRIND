class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])

        sums = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            cur = 0

            for j in range(1, n + 1):
                cur += matrix[i - 1][j - 1]

                sums[i][j] = cur + sums[i - 1][j]

        self.sums = sums

    def sumRegion(self, row1, col1, row2, col2):
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        bottom_right = self.sums[row2][col2]

        top = self.sums[row1 - 1][col2]
        left = self.sums[row2][col1 - 1]

        top_left = self.sums[row1 - 1][col1 - 1]

        return bottom_right - top - left + top_left
