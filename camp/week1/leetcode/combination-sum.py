class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans =[]
        curr =[]
        n=len(candidates)
        
        def com(i):
            nonlocal n
            if sum(curr)==target:
                ans.append(curr[:])
                return
            if sum(curr)>target:
                return
            for j in range(i,n): 
                curr.append(candidates[j])
                com(j)
                curr.pop()

        com(0)
        return ans
        