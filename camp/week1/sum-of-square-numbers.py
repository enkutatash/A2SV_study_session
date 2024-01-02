class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start=0
        end=int(sqrt(c))
        while start<=end:
            if start**2+end**2==c:
                print(start,end)
                return True
            elif start**2 + end**2>c:
                end-=1
            else:
                start+=1
        return False

        