class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles==0:
            return target-1
        ans=0
        while maxDoubles and target>1:
            if target%2!=0:
                ans+=1
                target-=1
            target//=2
            maxDoubles-=1
            ans+=1
        if target!=0:
            ans+=(target-1)
        return ans


        