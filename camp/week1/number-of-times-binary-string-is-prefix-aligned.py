class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        count=0
        total=0
        for i in range(len(flips)):
            total+=flips[i]
            if (i+1)*(i+2)/2==total:
                count+=1
        return count 

        