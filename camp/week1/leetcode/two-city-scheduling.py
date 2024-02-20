class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        groupA=[]
        groupB=[]
        for i in costs:
            if i[0]<=i[1]:
                groupA.append(i)
            else:
                groupB.append(i)
        if len(groupA)>len(groupB):
            groupA.sort(key=lambda a:abs(a[0]-a[1]))
            while len(groupA)>len(groupB):
                k=groupA[0]
                groupA=groupA[1:]
                groupB.append(k)
        else:
            groupB.sort(key=lambda a:abs(a[0]-a[1]))
            while len(groupA)<len(groupB):
                k=groupB[0]
                groupB=groupB[1:]
                groupA.append(k)
        ans=0
        for i, v in zip(groupA,groupB):
            ans+=i[0]
            ans+=v[1]
        return ans
            
        
            
        