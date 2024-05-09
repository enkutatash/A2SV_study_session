class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = [(v,i) for i,v in enumerate(score)]
        s.sort(reverse = True)
        ans = [[] for i in range(len(score))]
        for i in range(len(score)):
            v,index = s[i]
            if i == 0:
                ans[index] = "Gold Medal"
            elif i == 1:
                ans[index] = "Silver Medal"
            elif i == 2:
                ans[index] = "Bronze Medal"
            else:
                ans[index] = str(i+1)
        return ans
        
            
        