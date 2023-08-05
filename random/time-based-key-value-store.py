class TimeMap:

    def __init__(self):
        self.timemap = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timemap:
            self.timemap[key] = ([],[])
        self.timemap[key][0].append(value)
        self.timemap[key][1].append(timestamp)

        

    def get(self, key: str, timestamp: int) -> str:
        # print("Get req",key,timestamp)
        if not key in self.timemap:
            return ""
        timeline = self.timemap[key][1]
        values = self.timemap[key][0]
        if timestamp<timeline[0]:
            return ""
        l,h=0,len(timeline)-1
        # print(timeline)
        while(l<=h):
            m=(l+h)//2
            print(l,m,h)
            if timeline[m]==timestamp:
                return values[m]
            elif timeline[m]>timestamp:
                h=m-1
            else:
                l=m+1
        return values[l - 1] if l > 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)