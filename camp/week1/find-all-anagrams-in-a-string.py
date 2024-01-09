class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        check=Counter(p)
        for i in range(len(s)-len(p)+1):
            sample=s[i:i+len(p)]
            if Counter(sample)==check:
                res.append(i)
        return res

       




        