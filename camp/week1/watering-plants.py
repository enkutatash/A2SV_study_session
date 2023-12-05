class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step=0
        c=capacity
        for i,v in enumerate(plants):
            if capacity>=v:
                capacity-=v
                step+=1
            else:
                step+=(i)
                step+=(i+1)
                capacity=c-v
        return step

        