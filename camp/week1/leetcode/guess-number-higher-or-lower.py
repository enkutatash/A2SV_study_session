# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def pick(l,r):
            if l>r:
                return
            mid = (l+r)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid)<0:
                return pick(l,mid-1)
            else:
                return pick(mid+1,r)
        return pick(1,n)
        