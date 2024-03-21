class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(banana):
            nonlocal h
            hr = 0
            for i in piles:
                hr+=(math.ceil(i/banana))
            return hr<=h
        ans = max(piles)
        def allpossibility(l,r):
            nonlocal ans
            if l>r:
                return
            mid = (l+r)//2
            if possible(mid):
                ans = min(ans,mid)
                return allpossibility(l,mid-1)
            else:
                return allpossibility(mid+1,r)
        allpossibility(1,max(piles))
        return ans
        
        
            

        