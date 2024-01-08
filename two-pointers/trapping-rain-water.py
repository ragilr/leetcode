class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        s = 0
        # n space complexity solution
        # left = [0]*l
        # right = [0]*l
        # m = height[0]
        # for i in range(1,l):
        #     left[i]=m
        #     m=max(m,height[i])
        # m = height[-1]
        # for j in range(l-2,-1,-1):
        #     right[j]=m
        #     m=max(m,height[j])
        # for i in range(1,l-1):
        #     s+=max(min(left[i],right[i])-height[i],0)

        l=0
        lmax=height[0]
        r=len(height)-1
        rmax=height[-1]
        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax,height[l])
                s+=lmax-height[l]                
            else:
                r-=1
                rmax=max(rmax,height[r])                
                s+=rmax-height[r]
        return s
        