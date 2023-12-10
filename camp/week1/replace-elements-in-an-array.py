class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        base={nums[i]:i for i in range(len(nums))}
        for i in range(len(operations)):
            replace= base[operations[i][0]]
            del base[operations[i][0]]
            base[operations[i][1]]=replace
        #print(base)
        l=[0]*len(nums)
        for i,v in base.items():
             l[v]=i
        return l

        