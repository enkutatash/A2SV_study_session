class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum={0:1}
        result=0
        cur=0
        for n in nums:
            cur+=n
            dif=cur-k
            result+=presum.get(dif,0)
            presum[cur]=1+presum.get(cur,0)
        return result
