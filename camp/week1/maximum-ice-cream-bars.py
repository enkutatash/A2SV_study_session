class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ice_Cream=[0]*max(costs)
        for i in costs:
            ice_Cream[i-1]+=1
        # print(ice_Cream)
        buy=0
        i=0
        while coins>=(i+1) and i<len(ice_Cream):
            while ice_Cream[i]>0 and coins>=(i+1):
                coins-=(i+1)
                buy+=1
                ice_Cream[i]-=1
            i+=1
        return buy


        