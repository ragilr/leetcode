class HitCounter:
    # self.q = 0
    def __init__(self):
        self.q = deque()
        
    def adjustTime(self, timestamp: int) -> None:
        while len(self.q)>0 and timestamp-self.q[0]>299:
            self.q.popleft()
        
    def hit(self, timestamp: int) -> None:
        self.adjustTime(timestamp)
        self.q.append(timestamp)
        # print(self.q)
        

    def getHits(self, timestamp: int) -> int:
        self.adjustTime(timestamp)
        # print(self.q)
        return len(self.q)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)