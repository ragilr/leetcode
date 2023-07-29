class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = deque()
        self.incr = [0]*maxSize
        

    def push(self, x: int) -> None:
        if(len(self.stack)<self.maxSize):
            self.stack.append(x)
        return 
        

    def pop(self) -> int:
        if(len(self.stack)==0):
            return -1
        top_index = len(self.stack)-1            
        top = self.incr[top_index]
        self.incr[top_index]=0
        return top+self.stack.pop()


    def increment(self, k: int, val: int) -> None:
        i = 0
        curr_size = len(self.stack)
        last_ind = min(k,self.maxSize,curr_size)
        while i<last_ind:
            self.incr[i]+=val
            i+=1
        return
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)