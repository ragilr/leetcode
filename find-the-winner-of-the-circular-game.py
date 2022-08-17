class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def helper(q,k,p):
            if len(q)==1:
                return q[0]
            temp=p-k
            while p>0:
                q.append(q.popleft())
                p-=1
            if p==0:
                q.pop()
                return helper(q,k,k)
            else:
                return helper(q,k,temp)
        q = deque()
        for i in range(1,n+1):
            q.append(i)
        return helper(q,k,k)