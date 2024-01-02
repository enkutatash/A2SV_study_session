class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        other=0
        while zero<len(nums):
            if nums[zero]==0:
                break
            zero+=1
        other=zero+1
        while other<len(nums):
            if nums[other]!=0:
                nums[zero],nums[other]=nums[other],nums[zero]
                other=zero
                zero+=1
            other+=1
                
        

