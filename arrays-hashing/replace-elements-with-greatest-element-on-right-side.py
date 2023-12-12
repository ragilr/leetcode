class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        g=arr[-1]
        j=len(arr)-2
        arr[-1]=-1
        while j > -1:
            # print(arr[j],g)
            if arr[j]>g:
                temp=arr[j]
                arr[j]=g
                g=temp
            else:
                arr[j]=g
            # print(arr[j],g,arr)
            j=j-1
        return arr