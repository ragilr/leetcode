class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def dfs(target,comb,start):
            if target==0:
                ret.append(comb.copy())
                return
            if target<0:
                return
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                dfs(target-candidates[i],comb,i)
                comb.pop()
        dfs(target,[],0)
        return ret