class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l=len(s)
        d=dict()
        e=dict()
        for i in range(l):
            if s[i] not in d and t[i] not in e:
                d[s[i]]=t[i]
                e[t[i]]=s[i]
            elif s[i] in d and d[s[i]]!=t[i]:
                return False
            elif t[i] in e and e[t[i]]!=s[i]:
                return False
        return True
            