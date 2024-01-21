class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0 
        r = len(arr)-1
        idx,val = 0,arr[0]
        while l<=r:
            m = (l+r)//2
            currDiff,prevDiff = abs(arr[m]-x),abs(val-x)
            if currDiff<prevDiff or (currDiff==prevDiff and arr[m]<val):
                val,idx = arr[m],m
            if arr[m]<x:
                l=l+1
            elif arr[m]>x:
                r=r-1
            else:
                break
        l=r=idx
        # print("starting idx",l)
        while r-l+1<k and l>0 and r<len(arr)-1:
            if abs(arr[l-1]-x)<abs(arr[r+1]-x):
                l=l-1
            elif abs(arr[l-1]-x)==abs(arr[r+1]-x) and arr[l-1]<arr[r+1]:
                l=l-1
            else:
                r+=1
            # print(l,r)
        r = min(r,len(arr))
        l = max(l,0)
        while r-l+1<k and l>0:
            l=l-1
            # print(l,r)
        while r-l+1<k and r<len(arr):
            r+=1
            # print(l,r)
        return arr[l:r+1]
        # return [1]