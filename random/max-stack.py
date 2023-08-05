class MaxStack:
    
    maxStack=[]
    stack=[]
    
    def __init__(self):
        self.maxStack=[]
        self.stack=[]

    def push(self, x: int) -> None:
        if len(self.maxStack) > 0:
            m = max(self.peekMax(),x)
        else:
            m = x
        self.stack.append(x)
        self.maxStack.append(m)
        

    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def peekMax(self) -> int:
        return self.maxStack[-1]
        

    def popMax(self) -> int:
        m = self.peekMax()
        poppedItems=[]
        while self.top() != m:
            poppedItems.append(self.pop())
        self.pop()
        poppedItems.reverse()
        print(poppedItems)
        for popped in poppedItems:
            self.push(popped)
        return m
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()