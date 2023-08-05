class Solution:
    d = dict()
    def __init__(self):
        self.d[0]=0
        self.d[1]=1
    def fib(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        self.d[n]=self.fib(n-1)+self.fib(n-2)
        return self.d[n]