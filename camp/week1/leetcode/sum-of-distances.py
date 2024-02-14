class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        maped=defaultdict(list)
        answer=[0]*len(nums)
        for i,v in enumerate(nums):
            if len(maped[v])==0:
                maped[v].append([i,i]) 
            else:
                end=maped[v][-1][1]+i
                maped[v].append([i,end])
        for i,v in maped.items():
            if len(v)!=1:
                end=v[-1][1]
                z=len(v)
                for l,m in enumerate(v):
                    n,p=m
                    result=(n*(l+1)-p)+(end-p-((z-l-1)*n))
                    answer[n]=result
        return answer
            

        
        