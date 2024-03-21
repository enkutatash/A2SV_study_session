class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            j=i
            while nums[j]!=i+1:
                x = nums[j]
                if nums[x-1] == x:
                    break
                nums[j],nums[x-1]= nums[x-1],nums[j]
                j = i
        ans = []
        for i in range(len(nums)):
            if nums[i]!=i+1:
                ans.append(i+1)
        return ans
        
        