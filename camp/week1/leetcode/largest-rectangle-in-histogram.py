class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rectangle_area = 0
        stack = []
        removed = [0,0]
        n=len(heights)
        for i, v in enumerate(heights):
            first = i
            
            while stack and stack[-1][1]>v:
                removed = stack.pop()
                rectangle_area = max(rectangle_area,(i-removed[0])*removed[1])
                first = removed[0]
            
            stack.append([first,v])
        while stack:
            removed = stack.pop()
            rectangle_area = max(rectangle_area,(n-removed[0])*removed[1])
        
        return rectangle_area
            

        
        