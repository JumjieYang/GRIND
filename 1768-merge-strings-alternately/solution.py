class Solution:
    def merge_alternately(self, word1, word2):
        m, n = len(word1), len(word2)

        if m == 0:
            return word2

        if n == 0:
            return word1

        i = j = 0

        res = []

        from_first = True

        while i < m and j < n:
            if from_first:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1

            from_first = not from_first

        while i < m:
            res.append(word1[i])
            i += 1

        while j < n:
            res.append(word2[j])
            j += 1

        return ''.join(res)
