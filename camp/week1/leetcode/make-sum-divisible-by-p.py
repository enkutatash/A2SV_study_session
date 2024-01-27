class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p==0:
            return 0
        if sum(nums)<p:
            return -1
        remain=sum(nums)%p
        map={0:-1}
        ans=float('inf')
        k=0
        for i in range(len(nums)):
            k+=nums[i]
            k%=p
            if (k-remain)%p in map:
                ans=min(ans,i-map[(k-remain)%p])
            map[k]=i
        return ans if  ans<len(nums) else -1
