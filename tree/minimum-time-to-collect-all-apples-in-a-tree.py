class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        neigh = { i:[] for i in range(n)}
        for edge in edges:
            a,b = edge[0],edge[1]
            neigh[a].append(b)
            neigh[b].append(a)
        def dfs(node,parent):
            ret=0
            for n in neigh[node]:
                if n == parent:
                    continue
                time = dfs(n,node)
                if time or hasApple[n]:
                    ret += time+2
            # print("going back from ",node," at ",ret)
            return ret
        return dfs(0,-1)