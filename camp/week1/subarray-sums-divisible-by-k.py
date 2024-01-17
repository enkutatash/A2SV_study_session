class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remain=defaultdict(int)
        remain[0]=1
        sumup=0
        ans=0
        for right in nums:
            sumup+=right
            z=sumup%k
            ans+=remain[z]
            remain[z]+=1
        return ans
            
        