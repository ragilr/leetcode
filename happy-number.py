class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        s = set()
        s.add(n)
        n = self.sumOfDigits(n)
        while n not in s:
            if n == 1:
                return True
            s.add(n)
            n = self.sumOfDigits(n)
            
        return False
        
    def sumOfDigits(self, n: int)-> int:
        s = 0
        while n > 0:
            d = n%10
            s+= d*d
            n=n//10
        print(s)
        return s