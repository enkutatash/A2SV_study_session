class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closed=float("inf")
        for i in range(len(nums)):
            start=i+1
            end=len(nums)-1
            while start<end:
                check=nums[i]+nums[start]+nums[end]
                if abs(target-check)<abs(target-closed):
                    closed=check
                if check>target:
                    end-=1
                else:
                    start+=1
        return closed
        

        