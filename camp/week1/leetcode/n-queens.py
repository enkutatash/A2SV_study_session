class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []

        def putQueen(i, avC, avD1, avd2, curr):
            if i == n:
                ans.append(["".join(k) for k in curr])
                return
            
            for j in range(n):

                if j not in avC and  (i + j) not in avD1 and (i - j) not in avd2:
                    curr[i][j] = 'Q'

                    avC.add(j)
                    avD1.add( i + j)
                    avd2.add(i - j)

                    putQueen(i + 1, avC, avD1, avd2, curr)

                    curr[i][j] = '.'
                    avC.remove(j)
                    avD1.remove( i + j)
                    avd2.remove(i - j)
        for i in range(n):
            curr = [['.']*n for i in range(n)]
            curr[0][i] = 'Q'
            putQueen(1, set([i]),set([i]),set([-i]),curr)
        return ans
            

















