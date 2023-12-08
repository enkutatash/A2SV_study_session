class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        samecontent=defaultdict(list)
        for i in paths:
            key,*file=i.split()
            for j in file:
                name,*content=j.split('(')
                onefile=f"{key}/{name}"
                k="".join(content)
                samecontent[k].append(onefile)
                
        result=[i for i in samecontent.values() if len(i)>1]
        return result
        
        
    
        


        