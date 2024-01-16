class NumArray:

    def __init__(self, nums: List[int]):
        self.ans=[0]
        sumi=0
        for i in nums:
            sumi+=i
            self.ans.append(sumi)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.ans[right+1]-self.ans[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)