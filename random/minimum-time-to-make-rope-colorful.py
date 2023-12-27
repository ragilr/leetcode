class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        j = i+1
        ret = 0
        # print(colors)
        while j<len(colors):
            s = 0
            # print(colors[i],colors[j])
            if colors[j]==colors[i]:
                s = neededTime[i]
                m = neededTime[i]
                while j<len(colors) and colors[j]==colors[i]:
                    # print(colors[i],colors[j])
                    s+=neededTime[j]
                    m = max(m,neededTime[j])
                    j+=1
                s-=m
            ret+=s
            i=j
            j=i+1
        # print("ret",ret)
        return ret