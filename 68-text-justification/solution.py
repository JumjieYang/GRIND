class Solution:
    def fully_justify(self, words, maxWidth):
        res = []
        line, width = [], 0

        for word in words:
            if width + len(line) + len(word) > maxWidth:
                extra = maxWidth - width

                space = extra // max(1, len(line) - 1)
                remain = extra % max(1, len(line) - 1)

                for i in range(max(1, len(line) - 1)):
                    line[i] += ' ' * space

                    if remain:
                        line[i] += ' '
                        remain -= 1

                res.append(''.join(line))
                line, width = [], 0

            line.append(word)
            width += len(word)

        last = ' '.join(line)

        width = maxWidth - len(last)

        res.append(last + ' ' * width)

        return res
