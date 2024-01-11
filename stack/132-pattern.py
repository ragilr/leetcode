class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s = deque()
        m = float('inf')
        for n in nums:
            while s and s[-1][0]<=n:
                s.pop()
            if s and n < s[-1][0] and n > s[-1][1]:
                return True
            s.append((n,m))
            m = min(m,n)
        return False
