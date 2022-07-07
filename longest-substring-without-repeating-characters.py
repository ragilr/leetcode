class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        wi=-1
        w=0
        ans=float('-inf')
        i=0
        m=0
        # print(s)
        if len(s)==0:
            return 0
        while i < len(s):
            # print(d,s[i],w,m)
            if s[i] not in d:
                w+=1
                d[s[i]]=i
            else:
                for k in list(d.keys()):
                    if d[k] < d[s[i]]:
                        del d[k]
                w = i-d[s[i]]
                d[s[i]]=i
            ans = max(w,ans)
            i+=1
        return ans