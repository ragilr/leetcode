from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # solved using djikstra algorithm
        wordSet = set()
        wAdj = dict()
        visited = dict()
        dist = dict()
        for w in wordList:
            wordSet.add(w)
            visited[w]=False
            dist[w]=float('Inf')
        if endWord not in wordSet:
            return 0
        q = deque()
        q.append(beginWord)
        dist[beginWord]=1
        while q:
            w=q.popleft()
            visited[w]=True
            adj = []
            if w in wAdj:
                adj = wAdj[w]
            else:
                adj = self.wordGen(w,wordSet)
                wAdj[w] = adj
            for a in adj:
                if not visited[a]:
                    q.append(a)
                    if dist[a]>dist[w]+1:
                        dist[a]=dist[w]+1
        if dist[endWord] == float('inf'):
            return 0
        return dist[endWord]
    
    def wordGen(self,word: str, wordSet:set) -> List[str]:
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        w = []
        for i in range(len(word)):
            for a in alpha:
                if a!=word[i]:
                    s=word[:i]+a+word[i+1:]
                    if s in wordSet:
                        w.append(s)
        return w
            