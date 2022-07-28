class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        index = []
        ret = [0]*len(temperatures)
        i=0
        while i < len(temperatures):
            t=temperatures[i]
            if len(stack)==0:
                stack.append(t)
                index.append(i)
            else:
                while len(stack)>0 and t>stack[-1]:
                    stack.pop()
                    j = index.pop()
                    ret[j]=i-j
                stack.append(t)
                index.append(i)
            i+=1
        return ret