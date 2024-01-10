class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = deque()
        # positive meaning right, negative meaning left
        for a in asteroids:
            # if q and q[-1]>0 and a<0 and q[-1]==-a:
            #     q.pop()
            #     continue
            c = a
            eq = False
            while q and q[-1]>0 and c<0:
                if abs(q[-1])>abs(c):
                    c=q.pop()
                elif q[-1]==-c:
                    eq = True
                    q.pop()
                    break
                else:
                    q.pop()
            if not eq:
                q.append(c)
            # print(a,q)
        return list(q)