class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products=[1]*(len(nums)+1)
        
        for i in range(1,len(nums)):
            products[i]=products[i-1]*nums[i-1]
        right=1
        for i in range(len(nums)-1,-1,-1):
            products[i]*=right
            right*=nums[i]
        return products[:-1]

        
        