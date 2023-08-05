class Vector2D:
    vec = []
    n = 0
    pi = 0
    pj = 0
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.pi = 0
        self.pj = 0
        self.n=0
        i = 0
        while i < len(vec):
            j=0
            while j < len(vec[i]):
                self.n+=1
                j+=1
            i+=1
        
        

    def next(self) -> int:
        if self.pj >= len(self.vec[self.pi]):
            self.pj=0
            self.pi+=1
            while len(self.vec[self.pi])==0:
                self.pi+=1
        ret = self.vec[self.pi][self.pj]
        self.pj+=1
        self.n-=1
        # print(self.n)
        return ret

    def hasNext(self) -> bool:
        return (self.n > 0)
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()