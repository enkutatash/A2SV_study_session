class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        maxi1=[]
        maxi2=[]
        ans=0
        gridT=[[0]*c for i in range(r) ]
        for r1 in range(r):
            for c1 in range(c):
                gridT[c1][r1]=grid[r1][c1]
        for r1,r2 in zip(grid,gridT):
            mG1=max(r1)
            mG2=max(r2)
            maxi1.append(mG1)
            maxi2.append(mG2)
        for i in range(r):
            for j in range(c):
                added=min(maxi1[i],maxi2[j])
                ans+=(added-grid[i][j])
        return ans

            

        
            



        
        



        