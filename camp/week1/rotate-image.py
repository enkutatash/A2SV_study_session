class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat=list(zip(*matrix))
        for i in range(len(mat)):
            matrix[i]=list(reversed(mat[i]))
        
        