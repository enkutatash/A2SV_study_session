class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        li=sorted(points,key=lambda a:a[0])
        maxi=0
        
        for i in range(len(li)-1):
            maxi=max(maxi,(li[i+1][0]-li[i][0]))
        return maxi
        