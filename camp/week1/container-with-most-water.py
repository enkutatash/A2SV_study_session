class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxv=0
        while left<right:
            volume=min(height[left],height[right])*(right-left)
            maxv=max(maxv,volume)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maxv
        