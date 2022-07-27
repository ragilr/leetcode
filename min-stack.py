class MinStack:
    stack=[]
    minStack=[]
    def __init__(self):
        self.stack=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        m = float('inf')
        if len(self.minStack)>0:
            m=self.minStack[-1]
        if val<=m:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        top=self.stack[-1]
        m = self.minStack[-1]
        if top==m:
            self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()