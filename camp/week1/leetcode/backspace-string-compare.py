class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        finalS=[]
        for i in s:
            if i!='#':
                finalS.append(i)
            else:
                if finalS :
                    finalS.pop()
        finalT=[]
        for i in t: 
            if i!='#':
                finalT.append(i)
            else:
                if finalT:
                    finalT.pop()
        return finalS==finalT

        