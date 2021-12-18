class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        d={}
        for n in nums1:
            d[n] = d.get(n,0) + 1
        print(d,nums1,nums2)
        res = []
        for n in nums2:
            if n in d and d[n]>0:
                d[n]-=1
                res.append(n)
            # print(d)
        return res
            
        