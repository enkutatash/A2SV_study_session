class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        curr = []
        # val = None

        def sub(i):
            if i>=len(nums):
                curr2= tuple(sorted(curr))
                ans.add(curr2)
                return
            
            curr.append(nums[i])
            sub(i+1)
            curr.pop()
            sub(i+1)
        sub(0)
        return list(ans)

        