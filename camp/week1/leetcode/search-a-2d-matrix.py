class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchrow(top,bot):
            nonlocal target
            if top>bot:
                return -1
            mid = (top+bot)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                return mid
            elif matrix[mid][0]>target:
                return searchrow(top,mid-1)
            else:
                return searchrow(mid+1,bot)
        def searchcoln(left,right,row):
            nonlocal target
            if left>right:
                return False
            mid = (left+right)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                return searchcoln(left,mid-1,row)
            else:
                return searchcoln(mid+1,right,row)
            
        row = searchrow(0,len(matrix)-1)
        if row==-1:
            return False
        return searchcoln(0,len(matrix[0])-1,row)
        
            
