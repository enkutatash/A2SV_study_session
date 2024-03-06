# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        def Bad(l,r):
            if l>=r:
                return l
            mid = (l+r)//2
            if isBadVersion(mid):
                return Bad(l,mid)
            else:
                return Bad(mid+1,r)
        return Bad(1,n)

        