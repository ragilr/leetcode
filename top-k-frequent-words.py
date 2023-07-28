class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=dict()
        for w in words:
            d[w] = d.get(w,0)+1
        # print(d)
        words_sorted = sorted(d.items(),key = lambda x:(-x[1],x[0]))
        ret = []
        for i in range(k):
            ret.append(words_sorted[i][0])
        return ret