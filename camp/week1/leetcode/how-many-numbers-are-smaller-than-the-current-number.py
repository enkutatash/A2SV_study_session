class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=nums[:]
        ans=[]
        for n in range(len(nums)):
            mini=n
            for j in range(n+1,len(nums)):
                if nums[j]<nums[mini]:
                    mini=j
            nums[n],nums[mini]=nums[mini],nums[n]
        for i in range(len(nums)):
            ans+=[nums.index(l[i])]
        return ans
            

        