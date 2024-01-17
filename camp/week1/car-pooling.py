class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        takendistance=[0]*1001
        for i in trips:
            takendistance[i[1]]+=i[0]
            if i[2]<1000:
                takendistance[i[2]]-=i[0]
        sumup=0
        
        for i in takendistance:
            sumup+=i
            if sumup>capacity:
                return False
        return True
        