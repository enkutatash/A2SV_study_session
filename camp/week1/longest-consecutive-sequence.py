class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_no_rep=list(set(nums))
        maxi=1
        count=1
        nums_no_rep.sort()
        if len(nums)==0:
            return 0
        for i in range(1,len(nums_no_rep)):
            if nums_no_rep[i]==nums_no_rep[i-1]+1:
                count+=1
            else:
                count=1
            maxi=max(maxi,count)
        return maxi
