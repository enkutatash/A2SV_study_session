class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m={}
        for i in range(len(order)):
            m[order[i]]=i
        for i in range(len(words)-1):
            j=0
            while j<len(words[i]):
                if m[words[i][j]]<m[words[i+1][j]]:
                    break
                elif m[words[i][j]]>m[words[i+1][j]]:
                    return False
                elif j==len(words[i+1])-1 and j<len(words[i])-1:
                        return False
                elif m[words[i][j]]==m[words[i+1][j]]:
                    j+=1
                
                
        return True


        




        
        