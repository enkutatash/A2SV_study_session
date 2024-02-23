class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc_stk = deque()
        dec_stk = deque()

        invalid=-1
        ans=0
        for i,v in enumerate(nums):

            while inc_stk and nums[inc_stk[-1]]<=v:
                inc_stk.pop()
            inc_stk.append(i)
            while dec_stk and nums[dec_stk[-1]] >= v:
                dec_stk.pop()
            dec_stk.append(i)
            while  nums[inc_stk[0]]-v> limit:
                invalid=inc_stk[0]
                inc_stk.popleft()
            while  v- nums[dec_stk[0]] >limit:
                invalid=max(invalid,dec_stk[0])
                dec_stk.popleft()

            ans=max(ans,i-invalid)
        return ans

            


        