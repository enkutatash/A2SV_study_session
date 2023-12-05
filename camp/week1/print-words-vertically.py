class Solution:
    def printVertically(self, s: str) -> List[str]:
        k=s.split()
        maxi=0
        for i in k:
            maxi=max(maxi,len(i))
        ver={}
        for i in k:
            for j in range(maxi):
                if j>=len(i):
                    ver[j]=ver.get(j,"")+" "
                else:
                    ver[j]=ver.get(j,"")+i[j]
        vertical=[i.rstrip() for i in ver.values()]
        return vertical

        
        