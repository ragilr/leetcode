class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mxfreq = -1
        m = -1
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0)+1
            mxfreq = max(mxfreq,freq[s[r]])
            while r-l+1-mxfreq > k:
                freq[s[l]]-=1
                l+=1
            m = max(r-l+1,m)
            # print(l,r,freq,mxfreq,m)
        return m