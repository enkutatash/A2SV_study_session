class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        row = len(board)
        coln = len(board[0])

        def search(r,c,i):
            nonlocal row,coln
            if i>=len(word):
                return True
            if r>=row or c>=coln or r<0 or c<0 or board[r][c]!=word[i] or (r,c) in used:
                return 
            if board[r][c] == word[i]:
                used.add((r,c))
                val= search(r,c+1,i+1) or search(r+1,c,i+1) or search(r-1,c,i+1) or search(r,c-1,i+1)
                used.remove((r,c))
                if val:
                    return True
                    
            return False
        ans = False
        for R in range(row):
            for C in range(coln):
                ans = ans or search(R,C,0)
        return ans
        