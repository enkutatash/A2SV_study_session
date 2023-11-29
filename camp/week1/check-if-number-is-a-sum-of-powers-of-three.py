class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        r=0
        while n>0:
            r=n%3
            n=n//3
            if r==2:
                return False
        return True
        