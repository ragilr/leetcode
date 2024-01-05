class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        m=float('-inf')
        while i<j:
            w=j-i
            h = min(height[i],height[j])
            m=max(m,h*w)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return m