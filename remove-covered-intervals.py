class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: int(x[0]))
        ret = []
        ret.append(intervals[0])
        p = 0
        for i in range(1,len(intervals)):
            a=ret[p][0]
            b=ret[p][1]
            c=intervals[i][0]
            d=intervals[i][1]
            if a==c and d>=b:
                ret[p][1]=d
            elif b<d:
                ret.append(intervals[i])
                p=p+1
            print(ret)
        print(ret)
        return len(ret)

        