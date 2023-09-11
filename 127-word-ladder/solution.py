from collections import deque


class Solution:
    def ladder_length(self, beginWord, endWord, wordList):
        words = set(wordList)
        
        if endWord not in words:
            return 0
        
        q = deque([(beginWord, 1),])
        
        while q:
            node, cur = q.popleft()
            
            if node == endWord:
                return cur
            
            for i in range(len(node)):
                for c in string.ascii_letters:
                    word = node[:i] + c + node[i + 1:]
                    
                    if word in words:
                        words.remove(word)
                        
                        q.append((word, cur + 1))
        
        return 0