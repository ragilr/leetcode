class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        invalid=[]
        index=[]
        for i,c in enumerate(s):
            if c=='(':
                stack.append('(')
                index.append(i)
            elif c==')':
                if len(stack)>0:
                    stack.pop()
                    index.pop()
                else:
                    invalid.append(i)
        i=0
        j=0
        k=0
        ret=""
        while i<len(s):
            if len(invalid)>0  and len(invalid)>j and invalid[j]==i:
                j=j+1
            elif len(index)>0 and len(index)>k and index[k]==i:
                k+=1
            else:
                ret+=s[i]
            i+=1
        return ret