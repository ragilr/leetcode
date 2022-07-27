class Solution:
    def nextNum(self, s:str, i:int) -> List[int]:
        i=self.skipSpace(s,i)
        j=i
        c=s[j]
        while j<len(s) and c.isdigit():
            j+=1
            if j<len(s):
                c=s[j]
            num=int(s[i:j])
        return [num,j-1]
    
    def skipSpace(self,s:str, i:int) -> int:
        while i < len(s) and s[i]==' ':
            i+=1
        return i
            
    
    def calculate(self, s: str) -> int:
        stack = []
        i=0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                ret = self.nextNum(s,i)
                stack.append(ret[0])
                i=ret[1]
            elif c=='+':
                i+=1
                ret = self.nextNum(s,i)                
                stack.append(ret[0])
                i=ret[1]
            elif c=='-':
                i+=1               
                ret = self.nextNum(s,i)                
                stack.append(-ret[0])
                i=ret[1]
            elif c=='/':
                prev=stack.pop()
                i+=1                
                ret = self.nextNum(s,i)                
                i=ret[1]
                stack.append(int(prev/ret[0]))
            elif c=='*':
                i+=1       
                prev=stack.pop()
                ret = self.nextNum(s,i)                
                i=ret[1]
                stack.append(prev*ret[0])
            else:
                i=i
            i+=1
            # print(stack)
        return sum(stack)