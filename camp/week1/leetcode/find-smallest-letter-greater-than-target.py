class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = -1
        
        def binary(l,r):
            nonlocal ans
            if l>r:
                return 
            mid = (l+r)//2
            if ord(letters[mid])>ord(target):
                ans = mid
                return binary(l,mid-1)
            else:
                return binary(mid+1,r)
        binary(0,len(letters)-1)
        if ans ==-1:
            return letters[0]
        else:
            return letters[ans]
        
        