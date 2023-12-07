class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        all=[i for i in range(len(nums)+1)]
        for i in range(len(nums)):
            if nums[i]!=all[i]:
                return i
        return len(nums)
        
        