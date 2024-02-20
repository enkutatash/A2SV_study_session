class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans=0
        i=0
        check=set()
        for i in range(len(rolls)):
            check.add(rolls[i])
            if  len(check)==k:
                ans+=1
                check=set()
            
        return ans+1

        