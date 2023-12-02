class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pf = [0]*26
        l = len(p)
        for c in p:
            pf[ord(c)-ord('a')] += 1
        sf = [0]*26
        for c in s[:l]:
            sf[ord(c)-ord('a')] += 1
        # for 
        ret = []
        if pf==sf:
            ret.append(0)
        # print(sf,pf)
        for i in range(1,len(s)-l+1):
            # print(s[i:i+l],s[i-l],s[i+l-1])
            sf[ord(s[i+l-1])-ord('a')] += 1
            sf[ord(s[i-1])-ord('a')] -= 1
            if pf == sf:
                ret.append(i)
        return ret
        
