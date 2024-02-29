class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        connect = set()
        for connection in connections:
            x,y = connection[0],connection[1]
            connect.add((x,y))
            adj[x].append(y)
            adj[y].append(x)
        ret = 0
        visited = set()
        # print(adj,connect)
        def dfs(node):
            nonlocal ret
            # print("dfs",node)
            for edge in adj[node]:
                # print(node,'->',edge)
                if edge not in visited and (node,edge) in connect:
                    ret+=1
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge)
        visited.add(0)
        dfs(0)
        return ret