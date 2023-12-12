class UndergroundSystem:

    def __init__(self):
        self.under_ground=defaultdict(lambda:[0,0])
        self.initial=defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.initial[id]=[stationName,t]
        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        out=self.initial[id]
       
        self.under_ground[(out[0],stationName)][0]+=t-out[1]
        self.under_ground[(out[0],stationName)][1]+=1
        del self.initial[id]
        
        


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.under_ground[(startStation,endStation)][0]/self.under_ground[(startStation,endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)