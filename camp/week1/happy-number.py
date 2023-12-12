class Solution:
    def isHappy(self, n: int) -> bool:
        checked=set()
        while n>0:
            j=n
            sum1=0
            if n==1:
                return True
            while j>0:
                sum1+=(j%10)**2
                j//=10
            if sum1 in checked:
                return False
            else:
                checked.add(sum1)
                n=sum1
        return False

