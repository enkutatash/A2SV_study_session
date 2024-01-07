class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest=0
        check=1
        left=0
        if 0 not in nums:
            return len(nums)-1
        for ele in range(len(nums)):
            if nums[ele]==0:
                check-=1
            while check<0:
                if nums[left]==0:
                    check+=1
                left+=1
            longest=max(longest,ele-left)
        return longest


        