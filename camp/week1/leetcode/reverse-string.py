class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def subfun(l,s,r):
            if l>=r:
                return
            s[l],s[r]=s[r],s[l]
            subfun(l+1,s,r-1)
        subfun(0,s,len(s) -1)
