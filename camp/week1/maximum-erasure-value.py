class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sumup=0
        left=0
        window=defaultdict(int)
        maxsum=0
        for i in range(len(nums)):
            window[nums[i]]+=1
            while window[nums[i]]>1:
                sumup-=nums[left]
                window[nums[left]]-=1
                left+=1
            sumup+=nums[i]
            maxsum=max(maxsum,sumup)
        return maxsum




        