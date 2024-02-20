class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr=0
        c=0
        for i in nums:
            if i>n:
                break
            
            while i-1>curr:
                curr+=curr+1
                c+=1
            curr+=i
        while n>curr:
            curr+=curr+1
            c+=1
        return c

        