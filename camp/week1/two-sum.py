class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre={}
        for i,n in enumerate(nums):
            if target-n in pre:
                return i,pre[target-n]
            pre[n]=i
            
                