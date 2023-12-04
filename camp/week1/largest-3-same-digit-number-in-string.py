class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        k=""
        y=[]
        if len(nums)==3 and nums[0]==nums[1]==nums[2]:
            return str(nums)
        for i in range(len(nums)-2):
            if nums[i]==nums[i+1]==nums[i+2]:
                y.append(int(nums[i:i+3]))
        if len(y)==0:
            return ""
        else:
            maxi=max(y)
            if maxi==0:
                return "000"
            else:
                return str(maxi)



        