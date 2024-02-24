class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        visited=set()
        stack=[]
        for i in range(n*2):
            i%=n
            while stack and nums[stack[-1]]<nums[i]:
                end=stack.pop()
                if end not in visited:
                    ans[end]=nums[i]
                    visited.add(end)
            stack.append(i)
        return ans
                

        