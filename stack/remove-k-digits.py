class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = deque()

        for n in num:
            n = int(n)
            while s and k>0 and s[-1]>n:
                s.pop()
                k-=1
            s.append(n)
        while k:
            s.pop()
            k-=1
        while s and s[0]==0:
            s.popleft()
        return ''.join(map(lambda x:str(x),s)) if s else '0'