class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = deque()
        a = 1
        prev = ''
        for c in s:
            if stk and stk[-1][0]==c:
                stk[-1] = (c,stk[-1][1]+1)
            else:
                stk.append((c,1))
            while stk and stk[-1][1]==k:
                stk.pop()
        ret = ''
        while stk:
            c,count = stk.popleft()
            ret+=c*count 
                # count-=1
        return ret