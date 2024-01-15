class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        odds=0
        count=0
        sub=0
        for right in range(len(nums)):
            
            if nums[right]%2==1:
                odds+=1
                sub=0
            while odds==k:
                sub+=1
                if nums[left]%2==1:
                    odds-=1
                left+=1
            count+=sub
        return count

            
        
        



        
      