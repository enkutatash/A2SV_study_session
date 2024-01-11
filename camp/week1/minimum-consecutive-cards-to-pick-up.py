class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        pair=defaultdict(int)
        mincard=float("inf")
        left=0
        for right in range(len(cards)):
            pair[cards[right]]+=1
            while pair[cards[right]]>1:
                mincard=min(mincard,right-left+1)
                pair[cards[left]]-=1
                left+=1
        return mincard if mincard!=float("inf") else -1


        