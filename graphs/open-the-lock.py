class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        move = {'0000':0}
        visited = set()
        deadends = set(deadends)
        q = deque()
        q.append('0000')
        found = q[-1]==target
        while q and not found:
            for _ in range(len(q)):
                node = q.popleft()
                if node in deadends:
                    continue
                for i in range(4):
                    n = int(node[i])
                    nxt=n+1 if n!=9 else 0
                    prev=n-1 if n!=0 else 9
                    nxt=node[:i]+str(nxt)+node[i+1:]
                    prev=node[:i]+str(prev)+node[i+1:]
                    if nxt not in visited:
                        move[nxt]=move[node]+1
                        visited.add(nxt)
                        q.append(nxt)
                    if prev not in visited:
                        move[prev]=move[node]+1
                        visited.add(prev)
                        q.append(prev)
                    if prev==target or nxt == target:
                        found = True
        if target not in move:
            return -1
        return move[target]