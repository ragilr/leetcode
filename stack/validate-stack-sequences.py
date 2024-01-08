class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l = len(pushed)
        stack = deque()
        i=j=0
        while i<l and j<l:
            if stack and popped[j]==stack[-1]:
                stack.pop()
                j+=1
            else:
                stack.append(pushed[i])
                i+=1
        if i<l:
            return False
        while stack:
            if stack.pop()!=popped[j]:
                return False
            j+=1
        return True