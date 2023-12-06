class Solution:
    def totalMoney(self, n: int) -> int:
        total=0
        for i in range(n):
            current= i//7 + i%7 + 1
            total+=current
        return total
        