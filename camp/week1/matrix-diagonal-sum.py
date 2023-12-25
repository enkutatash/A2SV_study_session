class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        n=len(mat)
        z=len(mat[0])
        for i in range(n):
            for j in range(z):
                if i-j==0:
                    sum+=mat[i][j]
                if i+j==len(mat)-1:
                    sum+=mat[i][j]
        if n%2!=0:
            return sum-mat[n//2][z//2]
        else:
            return sum
        