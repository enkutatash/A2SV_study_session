class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        li=list()
        sumi=0
        for i in nums:
            sumi+=i
            li.append(sumi)
        return li
