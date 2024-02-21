class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        result=0
        nums=nums[::-1]
        currMax=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<=currMax:
                currMax=nums[i]
                continue
            z=nums[i]
            q=z//currMax
            result+=q-1
            z-=(q*currMax)

            if z:
                l=math.ceil(nums[i]/currMax)
                currMax=nums[i]//l
                result+=1
                
        return result
            
            
        