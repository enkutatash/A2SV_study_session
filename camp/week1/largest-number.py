class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]+nums[i]>nums[i]+nums[j]:
                    nums[j],nums[i]=nums[i],nums[j]

                   # print(nums)
        out="".join(nums)
        if int(out)==0:
            return out[0]
        return out
        