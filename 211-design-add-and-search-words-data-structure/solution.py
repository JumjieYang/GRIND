class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        cur = self.root

        for c in word:
            cur = cur.setdefault(c, {})

        cur['$'] = word

    def search(self, word):
        def helper(word, cur):
            for i, c in enumerate(word):
                if c in cur:
                    cur = cur[c]
                else:
                    if c != '.':
                        return False

                    for k in cur:
                        if k != '$' and helper(word[i + 1:], cur[k]):
                            return True
                    return False

            return '$' in cur

        cur = self.root

        return helper(word, cur)
