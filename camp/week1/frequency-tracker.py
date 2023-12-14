class FrequencyTracker:

    def __init__(self):
        self.tracker=defaultdict(int)
        self.fre=defaultdict(int)

    def add(self, number: int) -> None:
        self.fre[self.tracker[number]]-=1
        self.tracker[number]+=1
        self.fre[self.tracker[number]]+=1
        
        

    def deleteOne(self, number: int) -> None:
        self.fre[self.tracker[number]]-=1
        self.tracker[number]=max(0,self.tracker[number]-1)
        self.fre[self.tracker[number]]+=1

        

    def hasFrequency(self, frequency: int) -> bool:
        return self.fre[frequency]>0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)