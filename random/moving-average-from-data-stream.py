
class MovingAverage:
    
    maxSize = -1
    currSize = 0
    currSum = 0
    q = 0

    def __init__(self, size: int):
        self.maxSize = size
        self.currSize = 0
        self.currSum = 0
        self.q = deque()

    def next(self, val: int) -> float:
        pop = 0
        if self.currSize == self.maxSize:
            pop = self.q.popleft()
            self.currSize -= 1
        self.currSum -= pop
        self.currSum += val
        self.q.append(val)
        self.currSize += 1
        return (self.currSum/self.currSize)
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)