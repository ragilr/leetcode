class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        news=[]
        for i in range(len(s)):
            if s[i]=='#':
                if len(news)>0:
                    news.pop()
            else:
                news.append(s[i])
            
        newt=[]
        for i in range(len(t)):
            if t[i]=='#':
                if len(newt)>0:
                    newt.pop()
            else:
                newt.append(t[i])
        print(news,newt)
        return newt==news
        