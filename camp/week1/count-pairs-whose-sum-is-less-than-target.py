class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        i=0
        nums.sort()
        while i<len(nums):
            j=len(nums)-1
            while j>i and nums[i]+nums[j]>=target:
                j-=1
            count+=(j-i)
            i+=1
        return count
