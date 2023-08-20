class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root

        for c in word:
            cur = cur.setdefault(c, {})

        cur['$'] = word

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur:
                return False

            cur = cur[c]

        return '$' in cur

    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur:
                return False

            cur = cur[c]

        return cur is not None
