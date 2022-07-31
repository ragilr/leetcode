class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        added = 0
        for c in s:
            if c == '(':
                stack.append('(')
            else:
                if len(stack)>0 and stack[-1]=='(':
                    stack.pop()
                else:
                    added+=1
        while len(stack)>0:
            added+=1
            stack.pop()
        return added
        