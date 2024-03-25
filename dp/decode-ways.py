class Solution:
    def numDecodings(self, s: str) -> int:
        d = {len(s):1}
        def find(i):
            if i in d:
                return d[i]
            if s[i]=='0':
                return 0
            x = find(i+1)
            if i+1 < len(s) and (s[i]=='1' or (s[i] =='2' and s[i+1] in "0123456")):
                x+=find(i+2)
            d[i]=x
            return x
        return find(0)