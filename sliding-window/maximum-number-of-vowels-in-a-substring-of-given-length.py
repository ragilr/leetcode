class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        m = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in vowels:
                m+=1
        count = m
        # print(s[:k],m)
        for i in range(1,len(s)-k+1):
            if (s[i-1]) in vowels:
                count-=1
            if s[i+k-1] in vowels:
                count+=1
            # print(s[i:i+k],m)
            m = max(m,count)
        return m
