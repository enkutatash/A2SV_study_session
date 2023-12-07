class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums=set(i for i in range(left,right+1))
        all=set()
        for i in ranges:
            for j in range(i[0],i[1]+1):
                all.add(j)
        print(nums)
        print(all)
        if nums<=all:
            return True
        return False
        