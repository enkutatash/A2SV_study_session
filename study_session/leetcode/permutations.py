class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []
        n=len(nums)
        used = set()
        
        def perm(i):
            if len(bucket)==n :
                ans.append(bucket[:])
                return
            for j in range(n):
                if nums[j] not in used:
                    bucket.append(nums[j])
                    used.add(nums[j])
                    perm(j+1)
                    bucket.pop()
                    used.remove(nums[j])


        perm(0)
        return ans