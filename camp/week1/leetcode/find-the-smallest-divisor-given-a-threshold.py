class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sample_check(sample):
            nonlocal threshold
            curr=0
            for i in nums:
                curr+=(math.ceil(i/sample))
                if curr>threshold:
                    return False
            return True
        start= 1 
        end = max(nums)
        ans =max(nums)
        def ending(start,end):
            nonlocal ans
            if start>end:
                return
            mid = (start+end)//2
            if sample_check(mid):
                ans = min(ans,mid)
                ending(start,mid-1)
            else:
                ending(mid+1,end)
        ending(start,end)
        return ans



            

        