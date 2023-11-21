class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        d = dict()
        #mark first and last indexes of each char
        for index,c in enumerate(s):
            if c in d:
                d[c][1] = index
            else:
                d[c] = [index,index]
        
        #count unique char between each first and last
        for key,value in d.items():
            if value[0]!=value[1]:
                count+=len(Counter(s[value[0]+1:value[1]]))                
        return count