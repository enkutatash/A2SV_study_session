class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penality=customers.count('Y')
        total=[penality]
        for i in customers:
            if i=='Y':
                penality-=1
                total.append(penality)
            else:
                penality+=1
                total.append(penality)
        minP=min(total)
        return total.index(minP)
        