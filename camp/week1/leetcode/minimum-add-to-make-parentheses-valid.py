class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        count=Counter()
        ans=0
        for i in s:
            if i=='(':
                count[i]+=1
            else:
                if count['(']>0:
                    count['(']-=1
                else:
                    ans+=1
                
        ans+=count['(']
        return ans 

        