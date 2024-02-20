class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end=len(nums)
        start=nums[0]

        for i in nums[1:]:
            if start<=0:
                return False
            if i>=start:
                start=i
            else:
                start-=1
        return True



        