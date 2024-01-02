class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat=len(people)
        start=0
        end=len(people)-1
        while start<end:
            if people[start]+people[end]<=limit:
                boat-=1
                start+=1
            end-=1
        return boat

        