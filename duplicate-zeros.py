class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        i=j=0
        end=False
        while(i<l and j<l):
            # print(i,j,arr[i])
            if arr[i]==0:
                if j<l-1:
                    # print('inc j')
                    j=j+1
                else:
                    end=True
                    i=i+1
                    break                  
            i=i+1
            j=j+1
        # print(len(arr),i,j)
        # print(arr)
        i=i-1
        j=len(arr)-1
        if end:
            arr[j]=0
            j=j-1
            i=i-1
        while i>-1:
            # print(i,j,arr[i])
            if arr[i]==0:
                arr[j]=arr[j-1]=0
                j=j-1
            else:
                arr[j]=arr[i]
            # print(arr)
            i=i-1
            j=j-1