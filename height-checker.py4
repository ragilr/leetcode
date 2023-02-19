class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = []
        for h in heights:
            expected.append(h)
        c = 0
        expected.sort()
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                c+=1
        return c