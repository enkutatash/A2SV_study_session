class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mini=float("inf")
        for i in range(len(ghosts)):
            mini=min(abs(target[0]-ghosts[i][0])+abs(target[1]-ghosts[i][1]),mini)
        step=abs(target[0])+abs(target[1])
        return False if mini<=step else True
        