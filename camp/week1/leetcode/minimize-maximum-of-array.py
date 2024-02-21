class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total=0
        ans=0
        for i in range(len(nums)):
            total+=nums[i]
            ans=max(ans,(total+i)//(i+1))
        return ans
            

        