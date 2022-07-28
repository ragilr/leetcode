class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[-1]
        m = 0
        for i,h in enumerate(heights):
            while stack[-1]>-1 and heights[stack[-1]]>=h:
                currentHeight = heights[stack.pop()]
                currentWidth = i-stack[-1]-1
                m=max(m,currentHeight*currentWidth)
            stack.append(i)
        while stack[-1]>-1:
            currentHeight = heights[stack.pop()]
            currentWidth = len(heights)-stack[-1]-1
            m=max(m,currentHeight*currentWidth)            
        return m
        