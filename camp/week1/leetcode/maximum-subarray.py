class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        su=float('-inf')
        s=float('-inf')
        for i in nums:
            if su>=0:
                su+=i
            else:
                su=i
            s=max(su,s)
        return s
        