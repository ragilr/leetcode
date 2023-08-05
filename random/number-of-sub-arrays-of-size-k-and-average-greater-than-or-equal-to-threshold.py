class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k])
        i = k
        c = 0
        f = arr[0]
        if s/k >= threshold:
            c+=1
        print(f,s,c)
        for i in range(k,len(arr)):
            # print(s," add ",arr[i]," subs ",f," Result:",s+arr[i]-f)
            s = s+arr[i]-f
            f=arr[i-k+1]
            # print("new f pos",i-k+1," value:",f)
            if s/k >= threshold:
                c+=1
            # print(f,s,c)
        return c