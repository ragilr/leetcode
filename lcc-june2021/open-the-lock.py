import math
from collections import deque

class Solution:
    rot = {'0':['1','9'],'1':['2','0'],'2':['3','1'],'3':['4','2'],'4':['5','3'],'5':['6','4'],'6':['7','5'],'7':['8','6'],'8':['9','7'],'9':['0','8']}
    
    def openLock(self, deadends: List[str], target: str) -> int:
        if(target=="0000"):
            return 0
        if("0000" in deadends):
            return -1
        noPath = dict()
        for d in deadends:
            noPath[d] = True
            
        distance = [math.inf]*10000
        visited = [False]*10000
        distance[0] = 0
        q = deque()
        q.append(0)
        
        while q:
            # print(q)
            u = q.popleft();
            neigh = self.findNeighbours(noPath,u)
            if neigh:
                for n in neigh:
                    if(not visited[n]):
                        visited[n]=True
                        distance[n]=distance[u]+1
                        q.append(n)
                    if(n==int(target)):
                        return distance[n]
        return -1
    
    def findNeighbours(self, noPath, node):
        if(node>999):
            node = str(node)
        elif(node>99):
            node = '0'+str(node)
        elif(node>9):
            node = '00'+str(node)
        elif(node>0):
            node = '000'+str(node)
        else:
            node = '0000'
        # print(node)
        neigh = []
        for i in range(4):
            s1 = node[0:i]+self.rot[node[i]][0]+node[i+1:]
            s2 = node[0:i]+self.rot[node[i]][1]+node[i+1:]
            if not s1 in noPath:
                neigh.append(int(s1))
            if not s2 in noPath:
                neigh.append(int(s2))
        return neigh