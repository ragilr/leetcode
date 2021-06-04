class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hLarge = self.largestCut(h, horizontalCuts)
        vLarge = self.largestCut(w, verticalCuts)
        return (hLarge*vLarge)%1000000007

    def largestCut(self, l: int, cuts: List[int]) -> int:
        cuts.sort()
        lastCut = 0
        largeCut = -1
        for c in cuts:
            cut = c-lastCut
            if cut > largeCut:
                largeCut = cut
            lastCut = c

        cut = l - lastCut
        if cut > largeCut:
            largeCut = cut
        return largeCut