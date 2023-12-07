class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mat={}
        for i in matches:
          mat[i[0]]=mat.setdefault(i[0],0)
          mat[i[1]]=mat.get(i[1],0)+1
        winner=[]
        one_losser=[]
        for i in mat:
          if mat[i]==0:
            winner.append(i)
          elif mat[i]==1:
            one_losser.append(i)
        winner.sort()
        one_losser.sort()
        return [winner,one_losser]

        


        