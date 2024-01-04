class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        li=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    li.add((nums[i],nums[j],nums[k]))
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif sum>0:
                    k-=1
                else:
                    j+=1
        
        return list(li)
