class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substr = []
        l = 0
        letters = dict()
        r = 0

        def updateLetters(i,val):
            letters[s[i]]=letters.get(s[i],0)+val
            if letters[s[i]]<=0:
                del letters[s[i]]

        while r<len(s): 
            updateLetters(r,1)
            # print(l,r,letters)
            while(len(letters)>maxLetters or r-l+1>maxSize):
                updateLetters(l,-1)
                l+=1
                # print(l,r,letters)
            while r-l+1>=minSize:
                substr.append(s[l:r+1])
                updateLetters(l,-1)
                l+=1
                # print(l,r,letters)
            r+=1
        count = Counter(substr).most_common(1)
        # print(count,type(count))
        if len(count)==0:
            return 0
        return count[0][1]