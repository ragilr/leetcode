class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        # print(freq,c)
        for i,v in c.items():
            freq[v].append(i)
        ret = []
        # print(freq)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                ret.append(n)
                if k==len(ret):
                    return ret
