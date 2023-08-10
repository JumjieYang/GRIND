class Solution:
    def length_of_longest_substring(self, s):
        visited = set()

        l = r = 0
        longest = 0
        while r < len(s):
            if s[r] not in visited:
                visited.add(s[r])
                r += 1
            else:
                visited.remove(s[l])
                l += 1

            longest = max(longest, r - l)

        return longest
