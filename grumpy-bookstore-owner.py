class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s=0
        for i,g in enumerate(grumpy):
            if g==0:
                s+=customers[i]
                customers[i]=0
        m=0
        i=0
        rm=0
        while i<minutes:
            # print(i)
            m=m+customers[i]
            i=i+1
        rm=m
        while i<len(grumpy):
            # print(i)
            m=m-customers[i-minutes]
            m=m+customers[i]
            i+=1
            rm=max(m,rm)
        return rm+s
