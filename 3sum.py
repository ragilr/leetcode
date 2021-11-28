class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        d = dict()
        zc = 0
        for x in range(0,len(nums)):
            n = nums[x]
            if n==0:
                zc += 1
                continue
            it = self.twoSums(x,nums,-n)
            if(len(it)>0):
                for i in it:
                    cpy = i.copy()
                    cpy.sort()
                    if tuple(cpy) not in d:
                        ans.append(i)
                        d[tuple(cpy)]=1
                    
        # return [self.twoSums([1,2,3],5)]
        if zc >= 3:
            ans.append([0,0,0])
        return ans
    
    def twoSums(self, avoid:int,nums: List[int], target:int) -> List[int]:
        d = dict()
        ans = []
        for i in range(0,len(nums)):
            if i==avoid:
                continue
            n = nums[i]
            if target-n in d:
                ans.append([-target,n,target-n])
            d[n]=1
        # print(target,ans)
        return ans