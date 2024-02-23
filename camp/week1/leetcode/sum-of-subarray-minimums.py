class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        inc_stk = [[-1,-1]]
        min_sum = 0 
        final=[1]*len(arr)
        n=len(arr) 
        for i, v in enumerate(arr):
            while inc_stk[-1][0]>v:
                end,inx=inc_stk.pop()
                final[inx]*=(i-inx)

            final[i]*=(i-inc_stk[-1][1])
            inc_stk.append([v,i])
        while inc_stk and inc_stk[-1][1]!=-1:
            end,inx=inc_stk.pop()
            final[inx]*=(n-inx)

        for i in range(n):
            min_sum+=(final[i]*arr[i])
        return min_sum%(10**9 + 7)

            


            
            

        