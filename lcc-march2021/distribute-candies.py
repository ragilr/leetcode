class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d = dict()
        dist = 0
        for c in candyType:
            if not(c in d):
                dist += 1
                d[c]=1
        if (len(candyType)/2 < dist):
            dist = len(candyType)/2
        return int(dist)
