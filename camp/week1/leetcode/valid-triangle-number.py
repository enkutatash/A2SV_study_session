class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l=j+1
                r=n-1
                mid=(r+l)//2
                while l<=r:
                    mid=(r+l)//2
                    if nums[i]+nums[j]>nums[mid]:
                        l=mid+1
                    else:
                        r=mid-1
                ans+=(l-j-1)
        return ans