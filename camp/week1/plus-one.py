class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        digits[-1]+=1
        for i in range(len(digits)-1,0,-1):
            if digits[i]>9:
                digits[i-1]+=1
                digits[i]-=10
        if digits[0]>=10:
            digits[0]-=10
            digits.insert(0,1)
        return digits
        