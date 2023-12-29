class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        operation = 0
        mini=min(nums)
        index=nums.index(mini)
        i=0
        while i <index:
            while nums[i]==nums[i+1]:
                i+=1
            operation+=i+1
            i+=1
        return operation
        