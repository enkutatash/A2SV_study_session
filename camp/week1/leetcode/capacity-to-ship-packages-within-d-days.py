class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(load):
            nonlocal days
            day=1
            curr=0
            for i in weights:
                if curr+i <=load:
                    curr+=i
                else:
                    day+=1
                    curr=i
            return day<=days
        ans = sum(weights)
        def different(l,r):
            nonlocal ans
            if l>r:
                return
            mid = (l+r)//2
            if possible(mid):
                ans = min(ans ,mid)
                return different(l,mid-1)
            else:
                return different(mid+1,r)
        different(max(weights),sum(weights))
        return ans
            





