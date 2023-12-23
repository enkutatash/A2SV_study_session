class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
        return transposed
        