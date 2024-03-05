class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        curr = []
        if n==1:
            return []
        
        def combination(i):
            if sum(curr)==n and len(curr)==k:
                ans.append(curr[:])
                return
            if len(curr)>k or sum(curr)>n:
                return
            for j in range(i,10):
                curr.append(j)
                combination(j+1)
                curr.pop()
        combination(1)
        return ans