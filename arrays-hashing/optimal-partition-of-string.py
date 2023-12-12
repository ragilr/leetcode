class Solution:
    def partitionString(self, s: str) -> int:
        # d = [0]*26
        # count = 0
        # for c in s:
        #     index = ord(c)-97
        #     if d[index] == 1:
        #         count += 1
        #         for i in range(len(d)):
        #             d[i]=0
        #     d[index] = 1
        #     # print(c,d,count)
        # return count+1

        #below solution is faster!
        d=set()
        count=0

        for c in s:
            if c in d:
                count+=1
                d.clear()
            d.add(c)
        return count+1
