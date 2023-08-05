class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        d = dict()
        for i in range(n):
            d[i] = {i}
        # print(d)
        for l in logs:
            s = d[l[1]].union(d[l[2]])
            for i in s:
                d[i] = s
            # print(l,d)
            if len(d[l[1]]) == n:
                return l[0]
        return -1
        