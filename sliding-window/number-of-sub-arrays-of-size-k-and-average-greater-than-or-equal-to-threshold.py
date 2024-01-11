class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k])
        m = k*threshold
        c = 1 if s>=m else 0
        for i in range(1,len(arr)-k+1):
            s = s-arr[i-1]+arr[i+k-1]
            c = c+1 if s >= m else c
            # print(s,c)
        return c