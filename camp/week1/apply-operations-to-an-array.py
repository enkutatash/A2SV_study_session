class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
                i+=1
        write=0
        read=0
        while read<len(nums):
            if nums[read]!=0:
                nums[read],nums[write]=nums[write],nums[read]
                write+=1
            read+=1
        return nums

        