class Solution:
    def bestClosingTime(self, customers: str) -> int:
        l=len(customers)
        op = []
        close = []
        for c in customers:
            if c=='Y':
                close.append(1)
                op.append(0)
            else:
                op.append(1)
                close.append(0)
        for i in range(1,l):
            op[i]=op[i-1]+op[i]
            close[i]=close[i-1]+close[i]
        ret = float('inf')
        ret_index = float('inf')
        for i in range(l+1):
            c = close[-1] - (close[i-1] if i>0 else 0)
            o = op[i-1] if i>0 else 0
            # print("before",c,o,ret,ret_index)
            if ret > c+o:
                ret = c+o
                ret_index=i
            # print("after",c,o,ret,ret_index)
        # print(op)
        # print(close)
        return ret_index