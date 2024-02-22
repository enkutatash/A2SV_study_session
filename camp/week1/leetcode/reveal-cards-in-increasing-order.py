class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        first=sorted(deck)
        formed=deque()

        while first:
            last=first.pop()
            if formed:
                l=formed.popleft()
                formed.append(l)
            formed.append(last)
        formed.reverse()
        return formed
