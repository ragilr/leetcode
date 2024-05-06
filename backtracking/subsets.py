class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ret = [[]]
        # l = len(nums)
        # comb = 2**l
        # mask = 1
        # for i in range(1,comb):
        #     arr = []
        #     mask = 1
        #     print(i)
        #     for j in range(l):
        #         # print(i,j,mask&i)
        #         if(mask&i):
        #             arr.append(nums[j])
        #         mask=mask<<1
        #     ret.append(arr)         
        # return ret

        ret = []
        def dfs(i,sub):
            if i==len(nums):
                ret.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i+1,sub)
            sub.pop()
            dfs(i+1,sub)
        dfs(0,[])
        return ret            