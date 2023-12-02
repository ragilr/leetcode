class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        d = dict()
        count = 0
        for rect in rectangles:
            wh = rect[0]/rect[1]
            d[wh] = d.get(wh,0) + 1
        for value in d.values():
            count += (value*(value-1))/2
        return int(count)
        