class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            find = target - nums[i]
            search = bisect_right(nums,find)
            if search>=i:
                if search<n and nums[search]==find:
                    count+=(2**(search-i))
                elif search == i and nums[search]!=find:
                    count+=0
                else:
                    count+=(2**(search-i-1))
        return count % (10**9+7)

       