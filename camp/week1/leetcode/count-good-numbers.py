class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def powr(n,k):
            if k==0:
                return 1
            if k==1:
                return n
            else:
                if k%2!=0:
                    return n*powr(n,k-1)
                return powr(n*n %(10**9+7) , k//2)

        
        def count(n):
           
            if n%2==0:
                return (powr(4,n//2))*(powr(5,n//2))
            else:
                return (powr(5,math.ceil(n/2)))*(powr(4,n//2))
        ans=count(n)
        return ans%(10**9+7)
        