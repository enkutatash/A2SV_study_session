class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            i=j=0
            n=len(left)
            m=len(right)
            ans = []
            while i<n and j<m:
                if left[i]<=right[j]:
                    ans.append(left[i])
                    i+=1
                else:
                    ans.append(right[j])
                    j+=1
            while i<n:
                ans.append(left[i])
                i+=1
            while j<m:
                ans.append(right[j])
                j+=1
            return ans
        def mergesort(left,right,arr):
            if left==right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left = mergesort(left,mid,arr)
            right = mergesort(mid+1,right,arr)
            return merge(left,right)
        ans = mergesort(0,len(nums)-1,nums)
        return ans


        