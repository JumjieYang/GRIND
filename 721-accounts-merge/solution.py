class UF:
    def __init__(self):
        self.root = {}
    
    def find(self, x):
        y = self.root.get(x, x)
        
        if y != x:
            y = self.find(y)
            self.root[x] = y
        
        return y
    
    def union(self, x, y):
        self.root[self.find(x)] = self.find(y)


class Solution:
    def accounts_merge(self, accounts):
        pairs = set()

        uf = UF()
        for account in accounts:
            name = account[0]

            parent = None
            for email in account[1:]:
                pair = (name, email)

                if not parent:
                    parent = pair
                else:
                    uf.union(pair, parent)

                pairs.add(pair)

        associations = defaultdict(list)

        for pair in pairs:
            ancestor = uf.find(pair)

            associations[ancestor].append(pair[1])


        res = []

        for node in associations:
            entry = [node[0], ]

            for email in sorted(associations[node]):
                entry.append(email)

            res.append(entry)
        return res