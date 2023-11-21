class Solution:
    # def minSwaps(self, s: str) -> int:
    #     s=list(s)
    #     i = 0
    #     j = len(s)-1
    #     left = deque()
    #     right = deque()
    #     count = 0
    #     while i<j:
    #         stuck = False
    #         while i<len(s):
    #             c = s[i]
    #             if c == '[':
    #                 left.append('[')
    #             elif c==']' and len(left) and left[-1]=='[':
    #                 left.pop()
    #             else:
    #                 break
    #             i+=1
    #         while j>-1:
    #             c=s[j]
    #             if c==']':
    #                 right.append(']')
    #             elif c=='[' and len(right) and right[-1]==']':
    #                 right.pop()
    #             else:
    #                 break
    #             j-=1
    #         if i<len(s) and j>-1:
    #             s[i],s[j]=s[j],s[i]
    #             count+=1
    #         # print(s)
    #     return count
    def minSwaps(self, s: str) -> int:
        maxCount,count = 0,0
        for c in s:
            if c == '[':
                count -= 1
            else:
                count += 1
            maxCount = max(maxCount,count)
        return (maxCount+1)//2