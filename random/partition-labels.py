class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = dict()
        first = dict()
        for i,c in enumerate(s):
            last[c]=i
        
        ans=[]
        anchor=j=0
        for i,c in enumerate(s):
            j = max(j,last[c])
            if i==j:
                ans.append(i-anchor+1)
                anchor=i+1            
        return ans
        
        