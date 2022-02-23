"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # q = deque([node])
        # visited = dict()
        return self.dfs(node,dict())
    
    def dfs(self,node: 'Node',visited:dict) -> 'Node':
            if node==None:
                return None
            newNode = Node(node.val)
            visited[node]=newNode
            for n in node.neighbors:
                if n not in visited:
                    self.dfs(n,visited)
                newNode.neighbors.append(visited[n])
            return newNode
                    
            
            
        
        