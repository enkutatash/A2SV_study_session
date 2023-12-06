class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        merge=[]
        for i in range(n):
            merge.append(nums[i])
            merge.append(nums[i+n])
        return merge
        