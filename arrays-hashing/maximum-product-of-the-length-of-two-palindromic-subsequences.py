class Solution:
    def maxProduct(self, s: str) -> int:
        mp = float('-inf')          
        palenD = dict()

        def isPalenStr(index):
            nonlocal palenD
            tIndex = tuple(index)
            if tIndex in palenD:
                return palenD[tIndex]
            a = ''
            for i in index:
                a+=s[i]
            palenD[tIndex] = a == a[::-1]

        def subSeq(a,b,curr):
            # print(a,b,curr)
            nonlocal mp
            if curr==len(s):
                if isPalenStr(a) and isPalenStr(b):
                    mp = max(mp,len(a)*len(b))
                return
            a = list(a)
            b = list(b)
            c = list(a)
            d = list(b)
            a.append(curr)
            b.append(curr)
            subSeq(c,d,curr+1)
            subSeq(c,b,curr+1)
            subSeq(a,d,curr+1)
            
        subSeq([],[],0)
        return mp
    

    #more effiecient, bitmasking techinque
    def maxProduct(self, s: str) -> int:
        l = len(s)
        palen = dict()
        for i in range(1, 1<<l):
            a = ""
            for j in range(l):
                if i & (1<<j):
                    a += s[j]
            if a == a[::-1]:
                palen[i] = len(a)
        mx = 1
        print(palen)
        for i in palen:
            for j in palen:
                if i & j == 0:
                    mx = max(mx,palen[i]*palen[j])       
        return mx
        