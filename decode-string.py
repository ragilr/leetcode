class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i<len(s):
            c = s[i]
            if c.isdigit():
                j=i
                while c.isdigit():
                    i+=1
                    c=s[i]
                stack.append(int(s[j:i]))
                i=i-1
            elif c=='[':
                stack.append(c)
            elif c==']':
                temp=""
                while stack[-1]!='[':
                    temp+=stack.pop()
                # temp=temp[::-1]
                stack.pop() # pop [
                j = int(stack.pop())
                app = ""
                while j>0:
                    app+=temp
                    j-=1
                stack.append(app)
            else:
                stack.append(c)
            # print(stack)
            i+=1
        ret = ""
        while len(stack) > 0:
            ret+=stack.pop()
        return ret[::-1]
