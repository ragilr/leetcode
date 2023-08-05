class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s = s[::-1]
        print(d,s)
        a = d[s[0]]
        i = 1
        while i < len(s):
            if s[i] == 'I':
                if s[i-1] == 'V' or s[i-1] == 'X':
                    a-=1
                else:
                    a+=1
            elif s[i] == 'X':
                if s[i-1] == 'L' or s[i-1] == 'C':
                    a-=10
                else:
                    a+=10
            elif s[i] == 'C':
                if s[i-1] == 'D' or s[i-1] == 'M':
                    a-=100
                else:
                    a+=100
            else:
                a+=d[s[i]]
            i+=1
        return a