class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = len(s)
        appeared = set()
        if l<11:
            return []
        retset = set()
        appeared.add(s[:10])
        for i in range(1,l-10+1):
            # print('a')
            curr_str = s[i:i+10]
            # print(curr_str,appeared)
            if curr_str in appeared and curr_str not in retset:
                retset.add(curr_str)
            else:
                appeared.add(curr_str)
        return list(retset)
