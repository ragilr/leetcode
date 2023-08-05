class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        if h==0:
            return 0
        return self.binSearch(0,h,nums)
        
    
    
    def binSearch(self,l:int, h:int, n:List[int]) -> int:
        if(h-l==1 and n[h]>n[l]):
            return h
        elif(h-l==1 and n[l]>n[h]):
            return l
        mid = (l+h)//2
        length = len(n)
        if(mid>0 and mid<length-1 and n[mid]>n[mid-1] and n[mid]>n[mid+1]):
            return mid
        elif mid==0 and n[0]>n[1]:
            return 0
        elif mid==length-1 and n[length-1]>n[length-2] :
            return length-1
        elif n[mid-1]>n[mid] :
            return self.binSearch(l,mid-1,n)
        else:
            return self.binSearch(mid+1,h,n)
        
        