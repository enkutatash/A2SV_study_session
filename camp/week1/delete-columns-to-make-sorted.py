class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for j in range(len(strs[0])):
            s=[]
            for i in range(len(strs)):
                s.append(strs[i][j])
            if s!=sorted(s):
                count+=1
        return count
           
            
            


        