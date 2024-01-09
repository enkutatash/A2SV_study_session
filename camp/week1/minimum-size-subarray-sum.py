class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        left=0
        right=0
        sum1=0
        min_length=len(nums)
        while right<len(nums):
            sum1+=nums[right]
            while sum1>=target:
                min_length=min(min_length,right-left+1)
                sum1-=nums[left]
                left+=1
                
            right+=1
        return min_length



