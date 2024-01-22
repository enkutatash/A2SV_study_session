class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[]
        sumup=0
        for i in nums:
            prefix.append(sumup)
            sumup+=i
        suffix=[]
        total=sum(nums)
        for j in nums:
            total-=j
            suffix.append(total)

        result=[]
        for i in range(len(nums)):
            t=nums[i]*(i)-prefix[i]
            t+=suffix[i]-nums[i]*(n-i-1)
            result.append(t)
        return result

        