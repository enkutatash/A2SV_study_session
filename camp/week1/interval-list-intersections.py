class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans=[]
        first=0
        second=0
        if len(firstList)==0 or len(secondList)==0:
            return []
        
        while first<len(firstList) and second<len(secondList):
            i=max(firstList[first][0],secondList[second][0])
            j=min(firstList[first][1],secondList[second][1])
            if i<=j:
                ans.append([i,j])
            if firstList[first][1]<secondList[second][1]:
                first+=1
            else:
                second+=1
        return ans

        