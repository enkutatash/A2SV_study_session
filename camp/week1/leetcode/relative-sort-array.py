class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic={}
        for i in range(len(arr2)):
            dic[arr2[i]]=i
        k=sorted(arr1,key=lambda a:dic[a] if a in dic else len(arr2)+a)
        return k
        