class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            i=0
            j=0
            ans = []
            while i<len(left) or j<len(right):
                if i<len(left) and j<len(right):
                    if left[i]<=right[j]:
                        ans.append(left[i])
                        i+=1
                    else:
                        ans.append(right[j])
                        j+=1
                elif i<len(left):
                    ans.append(left[i])
                    i+=1
                else:
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


        