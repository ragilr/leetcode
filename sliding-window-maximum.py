class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ret = []
        m = float('-inf')
        i =0
        
        def cleanQ(i):
            if q and q[0]==i-k:
                q.popleft()
            while q and nums[i]>nums[q[-1]]:
                q.pop()
        
        
        q=deque()
        while i < k:
            cleanQ(i)
            q.append(i)
            m=max(nums[i],m)
            i+=1
        ret.append(m)
        
        
        
        for i in range(k,len(nums)):
            cleanQ(i)
            q.append(i) 
            ret.append(nums[q[0]])
        return ret
            
            
        