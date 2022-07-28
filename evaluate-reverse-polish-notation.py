class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(a+b)
            elif t== '-':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(b-a)
            elif t== '*':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(a*b)
            elif t== '/':
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(int(t))
            # print(stack)
        return stack[-1]
            