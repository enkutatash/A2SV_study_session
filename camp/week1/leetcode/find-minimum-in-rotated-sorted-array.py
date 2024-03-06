class Solution:
    def findMin(self, nums: List[int]) -> int:
       
        '''
        [0,1,2,3,4]
        [4,0,1,2,3]
        [3,4,0,1,2]
        [2,3,4,0,1]
        [1,2,3,4,0]
        '''
        
        def minimum(l,r):
            
            if l>=r:
                return nums[l]
            if nums[l]<nums[r]:
                return minimum(l,r-1)
            else:
                return minimum(l+1,r)
        
        return minimum(0,len(nums)-1)
                
            
