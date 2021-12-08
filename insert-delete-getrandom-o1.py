from random import choice

class RandomizedSet:
    a = []
    d = dict()
    def __init__(self):
        self.a = []
        self.d = dict()
        

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val]=len(self.a)
        self.a.append(val)
        # print(self.a,self.d)
        return True
        
        
        

    def remove(self, val: int) -> bool:
        if val in self.d:
            l,i = self.a[-1], self.d[val]
            self.a[i],self.d[l]=l,i
            self.a.pop()
            del self.d[val]
            # print(self.a,self.d)
            return True
        # print(self.a,self.d)
        return False
        

    def getRandom(self) -> int:
        # print(self.a,self.d)
        return choice(self.a)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()