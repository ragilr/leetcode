class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        def helper(first,sel):
            if len(sel)==k:
                ret.append(sel[:])
                return
            for i in range(first,n+1):            
                sel.append(i)
                helper(i+1,sel)
                sel.pop()
        helper(1,[])
        return ret