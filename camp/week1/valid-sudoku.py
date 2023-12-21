class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        coln=defaultdict(set)
        small_matrix=defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in row[i]:
                        return False
                    row[i].add(board[i][j])
                    if board[i][j] in coln[j]:
                        return False
                    coln[j].add(board[i][j])
                    if board[i][j] in small_matrix[(i//3,j//3)]:
                        return False
                    small_matrix[(i//3,j//3)].add(board[i][j])
            print(row)
            print(coln)
            print(small_matrix)
        return True
                    