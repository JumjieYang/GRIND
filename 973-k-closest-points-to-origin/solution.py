import random


class Solution:
    def k_closest(self, points, k):
        if len(points) <= k:
            return points

        def partition(l, r):
            idx = random.randint(l, r)

            pivot = points[idx][0] ** 2 + points[idx][1] ** 2

            points[r], points[idx] = points[idx], points[r]

            for i in range(l, r):
                cur = points[i][0] ** 2 + points[i][1] ** 2

                if cur <= pivot:
                    points[i], points[l] = points[l], points[i]
                    l += 1

            points[l], points[r] = points[r], points[l]

            return l

        l, r = 0, len(points) - 1

        while l < r:
            pivot = partition(l, r)

            if pivot == k:
                break
            elif pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1

        return points[:k]
