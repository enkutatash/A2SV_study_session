class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        i=0
        k=len(y)-1
        while(i<k):
            if y[i]!=y[k]:
                return False
            i+=1
            k-=1
            
        return True

        