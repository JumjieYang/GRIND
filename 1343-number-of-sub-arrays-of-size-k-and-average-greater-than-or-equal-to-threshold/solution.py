class Solution:
    def num_of_subarrays(self, arr, k, threshold):
        n = len(arr)

        sums = 0

        res = 0

        for i in range(k):
            sums += arr[i]

        if sums // k >= threshold:
            res += 1

        for i in range(k, n):
            sums += arr[i]
            sums -= arr[i - k]

            if sums // k >= threshold:
                res += 1

        return res
