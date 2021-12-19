class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        for c in s:
            a[ord(c)-ord('a')]+=1
        for c in t:
            a[ord(c)-ord('a')]-=1
        
        
        for i in a:
            if i!=0:
                return False
        return True