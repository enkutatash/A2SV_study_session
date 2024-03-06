class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius= float('-inf')
        n = len(heaters)
        localrad = 0
        for i in houses:
            left = bisect_left(heaters,i)
            if left<n and heaters[left]==i:
                localrad=0
            elif left == 0:
                localrad =heaters[0]-i
            elif left == n:
                localrad = i - heaters[-1]
            else:
                localrad = abs(i-heaters[left-1])
                localrad = min(localrad , abs(heaters[left]-i))
            
            radius = max(radius,localrad)
        return radius
            

        
        