class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans=0
        i=0
        while i<len(rolls):
            check=set()
            print(check)
            while i<len(rolls) and len(check)<k:
                check.add(rolls[i])
                i+=1
            if  len(check)==k:
                ans+=1
            print(check,i)
        return ans+1

        