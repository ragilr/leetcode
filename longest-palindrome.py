class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict()
        for i in s:
            d[i]=d.get(i,0)+1
        print(d)
        t=0
        once = False
        for k,v in d.items():
            if v%2==0:
                t+=v
            elif v>2 and not once:
                t+=v
                once = True
            elif v>2:
                t+=v-1
            elif not once:
                t+=1
                once = True
            print(k,v,t)
        return t
