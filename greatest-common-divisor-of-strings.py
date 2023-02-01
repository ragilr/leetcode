class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        a=len(str1)
        b=len(str2)
        l = min(a,b)
        gcd=1
        for i in range(2,l+1):
            if a%i==0 and b%i==0:
                gcd=i
        return str1[:gcd]
            