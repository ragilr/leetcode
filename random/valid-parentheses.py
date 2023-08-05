from collections import deque
class Solution:
    def isValid(self, st: str) -> bool:
        s=deque()
        for c in st:
            if c == '(' or c == '{' or c=='[':
                s.append(c)
            elif c==')' and len(s) and s[-1]=='(':
                s.pop()
            elif c==']' and len(s) and s[-1]=='[':
                s.pop()
            elif c=='}' and len(s) and s[-1]=='{':
                s.pop()
            else:
                return False
        if not s:
            return True
        return False
        