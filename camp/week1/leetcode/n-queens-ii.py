class Solution:
    def totalNQueens(self, n: int) -> int:

        ans = []
        curr = [['.']*n for i in range(n)]
        avC = set()
        avD1 = set()
        avd2 = set()

        def putQueen(i, avC, avD1, avd2):
            if i == n:
                ans.append(["".join(k) for k in curr])
                return
            
            for j in range(n):

                if j not in avC and  (i + j) not in avD1 and (i - j) not in avd2:
                    curr[i][j] = 'Q'

                    avC.add(j)
                    avD1.add( i + j)
                    avd2.add(i - j)

                    putQueen(i + 1, avC, avD1, avd2)

                    curr[i][j] = '.'
                    avC.remove(j)
                    avD1.remove( i + j)
                    avd2.remove(i - j)
        
        putQueen(0, avC,avD1,avd2)
        return len(ans)
            

















