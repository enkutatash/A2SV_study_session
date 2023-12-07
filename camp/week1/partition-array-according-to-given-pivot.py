class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        less_than_pivot = []
        greater_than_pivot = []
        equal_pivot = []

        for i in nums:

            if i<pivot:
                less_than_pivot.append(i)
            elif i==pivot:
                equal_pivot.append(i)
            else:
                greater_than_pivot.append(i)

        return less_than_pivot + equal_pivot + greater_than_pivot
        




        