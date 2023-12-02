
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(lambda x:str(x),nums)) #convert to str list
        nums.sort(key=LargerNumKey ) #sort
        return str(int("".join(nums))) #return and handle '000' case
        