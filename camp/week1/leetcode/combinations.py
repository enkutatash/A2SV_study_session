class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        bucket = []

        def backtrack(i):
            nonlocal k
            if len(bucket)==k:
                ans.append(bucket[:])
                return
            for z in range(i,n+1):
                bucket.append(z)
                backtrack(z+1)
                bucket.pop()
        backtrack(1)   
        return ans
        