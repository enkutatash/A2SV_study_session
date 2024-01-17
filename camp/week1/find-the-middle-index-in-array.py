class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        rightsum=sum(nums)
        leftsum=0
        left=0
        right=len(nums)
        while left<right:
            rightsum-=nums[left]
            if rightsum==leftsum:
                return left
            leftsum+=nums[left]
            left+=1
        return -1
        