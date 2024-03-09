class Solution:
    def jump(self, nums: List[int]) -> int:
        l , r = 0, 0
        n = len(nums)
        ans = 0 
        while r<n-1:
            max_jump = 0
            for j in range(l,r+1):
                max_jump = max(max_jump,j+nums[j])
            ans +=1
            l = r+1
            r = max_jump

        return ans

        


        