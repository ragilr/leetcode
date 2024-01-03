class Solution:
    #functions with 1 in suffix is hashmap implementation
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        ans = []
        d = dict()
        for x in range(0,len(nums)):
            n = nums[x]
            if( x > 0 and nums[x-1]==n):
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
        return ans
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if(nums[i]>0):
                break
            if(i==0 or nums[i]!=nums[i-1]):
                self.twoSums(i,nums,ans)
        return ans
    
    def twoSums(self, x:int, nums:List[int], res: List[List[int]]) -> List[int]:
        l = x+1
        r = len(nums)-1
        while(l<r):
            sum = nums[x]+nums[l]+nums[r]
            if(sum==0):
                res.append([nums[x],nums[l],nums[r]])
                l +=1
                r -=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
            elif sum>0:
                r-=1
            else:
                l+=1
                
        return res
                
        
    
    def twoSums1(self, avoid:int,nums: List[int], target:int) -> List[int]:
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


#Self second time
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        i=0
        # print(nums)
        def twoSum(target,l,h):
            c = []
            while l<h:
                curr = nums[l]+nums[h]
                # print('hello',target,l,h,nums[l],nums[h])
                if curr==target:
                    c.append([-target,nums[l],nums[h]])
                    while l+1< len(nums) and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                elif curr<target:
                    l+=1
                else:
                    h-=1
            # print(c)
            return c

        while i < len(nums)-2:
            # print('hi',i,nums[i],-nums[i])
            c = twoSum(-nums[i],i+1,len(nums)-1)
            if len(c)>0:
                # print("returned",ret,c)
                ret.extend(c)
                # print(ret,c)
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return ret


        

            