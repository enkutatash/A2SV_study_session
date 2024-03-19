class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        remain = defaultdict(int)
        sumup =0
        remain[0]+=1
        for i in nums:
            sumup+=i
            count+=remain[sumup%k]
            remain[sumup%k]+=1
        return count
        