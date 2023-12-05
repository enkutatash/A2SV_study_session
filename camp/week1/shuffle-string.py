class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=[0]*len(indices)
        for i,v in enumerate(indices):
            l[v]=s[i]
        return "".join(l)
