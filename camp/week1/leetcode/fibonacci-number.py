check={}
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: 
            return n
        first=0
        second=0
        if n-1 in check:
            first=check[n-1]
        else:
            first= self.fib(n-1)
            check[n-1]=first
        if n-2 in check:
            second= check[n-2]
        else:
            second=self.fib(n-2)
            check[n-2]=second
        return first + second
            

       
        