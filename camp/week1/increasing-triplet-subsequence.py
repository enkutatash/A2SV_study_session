class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first=float("inf")
        second=float("inf")
        for i in nums:
            if i>second:
                return True
            elif i>first:
                second=i
            else:
                first=min(i,first)
        return False

