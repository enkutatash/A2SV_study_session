class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum=0
        maxi=0
        for i in nums:
            if i==0:
                sum=0
            else:
                sum+=1
            maxi=max(sum,maxi)
        return maxi
        