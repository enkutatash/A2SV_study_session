class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            j= i
            while nums[j]!=i+1:
                x = nums[j]
                if nums[x-1] == x:
                    break
                nums[j],nums[x-1] = nums[x-1],nums[j]
                j = i
        ans = []
        for i,v in enumerate(nums):
            if v!=i+1:
                ans.extend([v,i+1])
        return ans

        