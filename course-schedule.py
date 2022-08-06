class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        edges = []
        for i in range(numCourses):
            edges.append([])
        for p in prerequisites:
            indegree[p[0]]+=1
            edges[p[1]].append(p[0])
        q=deque()
        for i,d in enumerate(indegree):
            if d == 0:
                q.append(i)
        order=[]
        while q:
            v = q.popleft()
            order.append(v)
            edge = edges[v]
            for e in edge:
                indegree[e]-=1
                if indegree[e]==0:
                    q.append(e)
        return len(order)==numCourses
            