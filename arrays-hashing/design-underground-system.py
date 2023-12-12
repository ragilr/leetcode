class UndergroundSystem:

    def __init__(self):
        self.inTransit = dict()
        self.travelTimeSum = dict()
        self.totalTravellers = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inTransit[id]=(stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInStation, startTime = self.inTransit[id]
        travelCode = checkInStation+'-'+stationName
        self.travelTimeSum[travelCode] = self.travelTimeSum.get(travelCode,0) + (t-startTime)
        self.totalTravellers[travelCode] = self.totalTravellers.get(travelCode,0) + 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travelCode = startStation+'-'+endStation
        return self.travelTimeSum[travelCode]/self.totalTravellers[travelCode]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)