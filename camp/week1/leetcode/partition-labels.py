class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rev=s[::-1]
        allcheck=defaultdict(list)
        n=len(s)
        for i in range(n):
            if s[i] not in allcheck:
                k=rev.index(s[i])
                allcheck[s[i]]=[i,n-k-1]
        start=allcheck[s[0]][0]
        end=allcheck[s[0]][1]
        ans=[]
        allcheck.pop(s[0])
        
        for v in allcheck.values():
            x1,x2=v
            if end>x1:
                end=max(end,x2)
            else :
                ans.append(end-start+1)
                start=x1
                end=x2
        ans.append(end-start+1)
        return ans
            



