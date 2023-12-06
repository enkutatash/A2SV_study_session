class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        increase_operation=0
        decrease_operation=0
        result1=True
        result2=True
        nums2=nums[:]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if increase_operation:
                    result1=False
                nums[i+1]=nums[i]
                increase_operation+=1

            if nums2[i]>nums2[i+1]:
                if decrease_operation:
                    result2=False
                nums2[i]=nums2[i+1]
                decrease_operation+=1
                if i-1>=0 and nums2[i]<nums2[i-1]:
                    result2=False
            
            
         
            
        return result1 or result2
        