class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seat=[0]*n
        for i in bookings:
            seat[i[0]-1]+=i[2]
            if i[1]<n:
                seat[i[1]]-=i[2]
        prefix=[]
        sumup=0
        for i in seat:
            sumup+=i
            prefix.append(sumup)
        return prefix


        