class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(c :str):
            return c in ['a', 'e', 'i', 'o', 'u']
        v = 0
        for i in range(min(k,len(s))):
            if isVowel(s[i]):
                v+=1
        m = v
        if len(s)<=k:
            return m
        for i in range(1,len(s)-k+1):
            if isVowel(s[i-1]):
                v=v-1
            if isVowel(s[i+k-1]):
                v=v+1
            m=max(m,v)
        return m