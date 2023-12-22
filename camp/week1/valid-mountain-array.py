class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag1=False
        flag2=True
        i=1
        while i<len(arr):
            if arr[i]>arr[i-1]:
                flag1=True
            elif arr[i]<arr[i-1]:
                break
            else:
                return False
            i+=1
        if flag1==True and i<len(arr):
            while i<len(arr):
                if arr[i]>=arr[i-1]:
                    return False
                i+=1
            flag2=True
        else:
            return False
        return flag1 and flag2
        

      
