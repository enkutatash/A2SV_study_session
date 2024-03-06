class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        n=len(citations)
        def citation(l,r):
            nonlocal n
            if l>r:
                return l
            mid = (l+r)//2
            if n-mid==citations[mid]:
                return mid
            elif n-mid>citations[mid]:
                return citation(mid+1,r)
            else:
                return citation(l,mid-1)
        
        return n - citation(0,len(citations)-1)

        
        