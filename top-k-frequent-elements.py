class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d =dict()
        for n in nums:
            d[n]=d.get(n,0)+1
        freq = []
        for key,value in d.items():
            freq.append([value,key])
        freq.sort(key = lambda x:x[0])
        # print(freq)
        ret=[]
        i = len(freq)-1
        while k>0:
            ret.append(freq[i][1])
            k-=1
            i-=1
        return ret
        