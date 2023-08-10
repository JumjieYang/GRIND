class Solution:
    def maximum_removals(self, s, p, removable):
        def is_subseq(s, p):
            i = j = 0

            while i < len(s) and j < len(p):
                if i in removed or s[i] != p[j]:
                    i += 1
                    continue

                i += 1
                j += 1

            return j == len(p)

        l, r = 0, len(removable) - 1

        while l <= r:
            mid = (l + r) // 2

            removed = set(removable[:mid + 1])

            if is_subseq(s, p):
                l = mid + 1
            else:
                r = mid - 1

        return l
