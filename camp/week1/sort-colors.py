class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            mini=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[mini]:
                    mini=j
            nums[mini],nums[i]=nums[i],nums[mini]
            
            






        