class Solution:
    def find_repeated_dna_sequences(self, s):
        res = set()
        visited = set()

        for i in range(len(s) - 9):
            cur = s[i: i + 10]

            if cur in visited:
                res.add(cur)

            visited.add(cur)

        return list(res)
