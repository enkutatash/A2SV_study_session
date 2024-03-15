class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        length=0
        for i in range(1,len(height)):
            length=min(max(height[:i]),max(height[i:]))
            if length>height[i]:
                water+=length-height[i]
        return water
            
        