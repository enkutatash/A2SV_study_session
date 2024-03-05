class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        n=len(nums)

        def sub(i):
            if i>=n:
                ans.append(curr[:])
                return
            curr.append(nums[i])
            sub(i+1)
            curr.pop()
            sub(i+1)           
        sub(0)
        return ans

        