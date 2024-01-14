class FreqStack:

    def __init__(self):
        self.mx = 0
        self.freq = {}
        self.fMap = {}
        

    def push(self, val: int) -> None:
        f = 1
        if val in self.freq:
            self.freq[val] += 1
            f = self.freq[val]
        else:
            self.freq[val] = 1
        self.mx = max(f,self.mx)
        if f in self.fMap:
            self.fMap[f].append(val)
        else:
            self.fMap[f] = deque([val])
        # print("Pushing",val)
        # print("Fmap",self.fMap)
        # print("Freq",self.freq)
        # print("Mx",self.mx)

        

    def pop(self) -> int:
        ret = self.fMap[self.mx].pop()
        self.freq[ret]-=1
        if len(self.fMap[self.mx]) == 0:
            self.mx -= 1
        # print("popping",ret)
        # print("Fmap",self.fMap)
        # print("Freq",self.freq)
        # print("Mx",self.mx)
        return ret
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()