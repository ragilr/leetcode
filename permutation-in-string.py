class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s = set()
        p = set()
        c = 0
        for n in nums:
            if k + n in s:
                a = (min(n,k+n),max(n,k+n))
                if a not in p:
                    p.add(a)
                    c+=1
            if -(k-n) in s:
                a = (min(n,-(k-n)),max(n,-(k-n)))
                if a not in p:
                    p.add(a)
                    c+=1
            s.add(n)
            # print(n,p)
        return c
