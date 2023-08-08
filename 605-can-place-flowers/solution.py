class Solution:
    def can_place_flowers(self, flowerbed, n):
        count = 0

        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 1:
                continue

            left = i == 0 or flowerbed[i - 1] != 1
            right = i == length - 1 or flowerbed[i + 1] != 1

            if left and right:
                flowerbed[i] = 1
                count += 1

        return count >= n
