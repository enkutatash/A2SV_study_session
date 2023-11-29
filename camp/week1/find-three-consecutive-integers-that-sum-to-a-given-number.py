class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n=num//3
        if n+n+n==num:
            return [n-1,n,n+1]
        else:
            return []
        