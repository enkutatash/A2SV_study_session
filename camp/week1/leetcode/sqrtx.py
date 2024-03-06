class Solution:
    def mySqrt(self, x: int) -> int:
        ans = -1

        def sqrt(l,r):
            nonlocal x,ans
            if l>r:
                return
            mid = (l+r)//2
            if mid*mid <= x:
                ans = mid
                return sqrt(mid+1,r)
            else:
                return sqrt(l,mid-1)

        sqrt(0,(x+1)//2)
        return ans
        