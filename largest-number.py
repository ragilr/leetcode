
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = []
        
        def numsort(a,b):
            return a+b > b+a
            
        
        for n in nums:
            s.append(str(n))
        s.sort(key=LargerNumKey )
        # s.sort(reverse=True )
        ret=""
        # print(s)
        for c in s:
            ret+=c
        if ret[0]=='0':
            return '0'
        return ret
        