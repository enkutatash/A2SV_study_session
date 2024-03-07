class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left =bisect_left(arr,x)
        right = bisect_right(arr,x)
        n=len(arr)


        if left==right and left>0 and right<n:
            left-=1
        elif left == right and left==0:
            right+=1
        elif left == right and left ==n :
            left-=1
        elif left+1!=right and left>=0 and right<n:
            left-=1
            
        if right-left-1>=k:
            return arr[left+1:left+k+1]
        while right-left-1<k:
            if left>=0 and right<n and abs(arr[left]-x)<=abs(arr[right]-x):
                left-=1
            elif left>=0 and right<n and abs(arr[left]-x)>abs(arr[right]-x):
                right+=1
            elif left<0 and right<n:
                right+=1
            else:
                left-=1
        return arr[left+1:right]
