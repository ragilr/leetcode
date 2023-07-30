class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # return nums

        def mergeSort(nums:List[int]):
            if len(nums)<=1:
                return nums
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            lsorted = mergeSort(left)
            rsorted = mergeSort(right)
            # ret = []
            l = 0
            r = 0
            k = 0
            while l<len(lsorted) and r<len(rsorted):
                # ret.append(min(lsorted[l],rsorted[r]))
                nums[k]=min(lsorted[l],rsorted[r])
                if lsorted[l]<=rsorted[r]:
                    l+=1
                else:
                    r+=1
                k+=1
            while l<len(lsorted):
                # ret.append(lsorted[l])
                nums[k] = lsorted[l]
                k+=1
                l+=1
            while r<len(rsorted):
                # ret.append(rsorted[r])
                nums[k]=rsorted[r]
                k+=1
                r+=1
            return nums
        return mergeSort(nums)

        def partition(l,h,arr):
            pivot_index = h
            pivot = arr[pivot_index]
            i = l-1
            for j in range(l,h):
                if arr[j]<=pivot:
                    i=i+1
                    arr[i],arr[j]=arr[j],arr[i]
                arr[i+1],arr[pivot_index]=arr[pivot_index],arr[i+1]
            return i+1
        
        def quickSort(l,h,arr):
            if l>=h:
                return
            pi = partition(l,h,arr)
            quicksort(l,pi-1,arr)
            quicksort(pi+1,h,arr)
        
        #quicksort
        # quicksort(0,len(nums)-1,nums)
        # return nums

        #mergesort
        return mergeSort(nums)