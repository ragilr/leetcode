class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l,h):
            mx = 0
            ret = ""
            while l>-1 and h<len(s) and s[l]==s[h]:
                mx = h-l+1
                ret = s[l:h+1]
                l-=1
                h+=1
            return ret

        ret = ""
        for i in range(len(s)):
            odd = helper(i,i)
            if len(odd)>len(ret):
                ret=odd
            even = helper(i,i+1)
            if len(even)>len(ret):
                ret=even
        return ret