class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hash=defaultdict(int)
        hash[0]=1
        sumup=0
        ans=0
        for i in nums:
            sumup+=i
            ans+=hash[sumup-goal]
            hash[sumup]+=1
        return ans