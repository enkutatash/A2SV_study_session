class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1=sum(nums[:k])
        maxsum=sum1
        right=0
        left=k
        while left<len(nums):
            sum1-=nums[right]
            sum1+=nums[left]
            maxsum=max(sum1,maxsum)
            left+=1
            right+=1
        return maxsum/k
