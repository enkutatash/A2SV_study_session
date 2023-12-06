class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority=set()
        compare=len(nums)/3
        for i in nums:
            if nums.count(i)>compare:
                majority.add(i)
        return list(majority)

        