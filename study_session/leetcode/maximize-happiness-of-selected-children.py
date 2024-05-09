class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        decrease = 0
        ans = 0
        happiness.sort()
        while k:
            remo = happiness.pop()
            if remo >= decrease:
                ans += (remo-decrease)
                decrease +=1
            k-=1
        return ans

        