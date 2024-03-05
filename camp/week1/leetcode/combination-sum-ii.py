class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = set()
        curr =[]
        n=len(candidates)
        
        def com(i):
            nonlocal n
            if sum(curr)==target:
                curr2=tuple(sorted(curr))
                ans.add(curr2)
                return
            if sum(curr)>target:
                return
            val = None
            for j in range(i,n): 
                if sum(candidates[j:])+sum(curr)<target:
                    continue
                if candidates[j]==val:
                    continue
                curr.append(candidates[j])
                com(j+1)
                val = curr.pop()

        com(0)
        return list(ans)