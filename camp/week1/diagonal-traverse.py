class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonal[i+j].append(mat[i][j])
        n=list()
        for i,v in diagonal.items():
            if i%2==0:
                v.reverse()
                n.extend(v)
            else:
                n.extend(v)
        return n
        