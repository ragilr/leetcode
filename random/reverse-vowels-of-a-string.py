def isvowel(c):
    c=c.lower()
    return (c=='a' or c=='e' or c == 'i' or c=='o' or c=='u') or ()

class Solution:
    
    
    def reverseVowels(self, s: str) -> str:
        v = []
        for c in s:
            if isvowel(c):
                v.append(c)
        rev = ""
        l = len(v)-1
        for c in s:
            if isvowel(c):
                rev+=v[l]
                l-=1
            else:
                rev+=c
        return rev