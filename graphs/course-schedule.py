class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0]*numCourses
        adj = defaultdict(list)
        for prereq in prerequisites:
            a,b = prereq
            inDegree[a]+=1
            adj[b].append(a)
        q = deque()
        for i,inDeg in enumerate(inDegree):
            if inDeg == 0:
                q.append(i)
        courseAttended = 0
        while q:
            course = q.popleft()
            for nei in adj[course]:
                inDegree[nei]-=1
                if inDegree[nei]==0:
                    q.append(nei)
            courseAttended+=1
        return courseAttended == numCourses