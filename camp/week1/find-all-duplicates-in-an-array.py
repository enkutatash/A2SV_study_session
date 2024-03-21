class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicate = set()
        ans = []
        for i in nums:
            if i in duplicate:
                ans.append(i)
            else:
                duplicate.add(i)
        return ans
        