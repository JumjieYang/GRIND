class Solution:
    def length_of_last_word(self, s):
        ptr = len(s) - 1

        length = 0

        while ptr > -1 and s[ptr] == ' ':
            ptr -= 1

        while ptr > -1 and s[ptr] != ' ':
            length += 1
            ptr -= 1

        return length
