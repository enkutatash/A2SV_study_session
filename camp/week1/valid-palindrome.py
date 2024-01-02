class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1=""
        for c in s.lower():
            if c.isalnum():
                s1+=c
        start=0
        end=len(s1)-1

        while start<end:
            if s1[start]!=s1[end]:
                return False
            start+=1
            end-=1
        return True