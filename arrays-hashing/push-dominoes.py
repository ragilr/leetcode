class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = list(dominoes)
        l = len(s)
        q = deque()
        visited=set()
        for i,v in enumerate(s):
            if v=='.':
                if i-1>-1 and s[i-1]=='R':
                    q.append(i)
                elif i+1<l and s[i+1]=='L':
                    q.append(i)
        # print(q)
        while q:
            s_temp = s.copy()
            n = len(q)
            while n:
                # print("".join(s),len(q))
                i = q.popleft()
                # print(i)
                visited.add(i)
                changed = False
                if i-1>-1 and s[i-1]=='R' and (i+1>=l or s[i+1]!='L'):
                    s_temp[i]='R'
                    changed = True
                elif i+1<l and s[i+1]=='L' and (i-1<0 or s[i-1]!='R'):
                    s_temp[i]='L'
                    changed = True
        
                if changed:
                    if i-1>-1 and s[i-1]=='.' and i-1 not in visited:
                        q.append(i-1)
                    if i+1<l and s[i+1]=='.' and i+1 not in visited:
                        q.append(i+1)
                # print("".join(s))
                n-=1
            s = s_temp
        return "".join(s)
        