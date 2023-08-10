from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.words = []


class Solution:
    def suggested_products(self, products, searchWord):
        root = TrieNode()

        products.sort()

        for product in products:
            cur = root

            for c in product:
                cur = cur.children[c]

                if len(cur.words) < 3:
                    cur.words.append(product)

        res = []
        cur = root
        for c in searchWord:
            cur = cur.children[c]

            res.append(cur.words)

        return res
