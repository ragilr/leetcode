class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m = dict()
        for a in nums1:
            for b in nums2:
                m[a+b] = m.get(a+b,0) + 1
        count = 0
        for c in nums3:
            for d in nums4:
                if -(c+d) in m:
                    count += m[-(c+d)]
                    
        
        return count
        