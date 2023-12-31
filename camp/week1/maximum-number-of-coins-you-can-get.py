class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        total=0
        piles.sort(reverse=True)
        l=len(piles)
        for i in range(1,l-l//3,2):
            total+=piles[i]
        return total
        