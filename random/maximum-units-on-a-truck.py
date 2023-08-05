class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        t=0
        i=0
        while truckSize>0 and i<len(boxTypes):
            if boxTypes[i][0]>0:
                truckSize-=1
                boxTypes[i][0]-=1
                t+=boxTypes[i][1]
            else:
                i+=1
        return t