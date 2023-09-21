class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ending = dict()
        s = sum(wall[0])
        for w in wall:
            l = 0
            for b in w:
                l += b
                if l!=s:
                    ending[l] = ending.get(l,0) + 1
        m = -1
        for k,v in ending.items():
            m = max(m,v)
            print(m,v)
        if m < 0:
            return len(wall)
        return len(wall)-m
