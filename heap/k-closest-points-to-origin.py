class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0,0]
        closest = []
        d = dict()
        for point in points:
            dist=math.dist(origin,point)
            if dist in d:
                d[dist].append(point)
            else:
                d[dist] = [point]
            if len(closest)<k:
                heapq.heappush(closest,-dist)
            else:
                heapq.heappushpop(closest,-dist)
        ret = []
        # print(closest,d)
        for close in closest:
            if -close not in d:
                continue 
            l = d[-close]
            # print(l)
            for i in l:
                ret.append(i)
            del d[-close]
        # print(ret)
        return ret

