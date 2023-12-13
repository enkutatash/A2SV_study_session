class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        element={}
        for i in cpdomains:
            visit,domain=i.split()
            indi=list(domain.split('.'))
            for j in range(len(indi)):
                element[".".join(indi[j:])]=element.get(".".join(indi[j:]),0)+int(visit)
        result=[f'{v} {i}' for i,v in element.items()]
        return result
                
            

        