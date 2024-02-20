class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans=0
        while numOnes and k:
            ans+=1
            k-=1
            numOnes-=1
        while numZeros and k:
            k-=1
            numZeros-=1
        while numNegOnes and k:
            k-=1
            numNegOnes-=1
            ans-=1
        return ans
        