class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort(reverse=True)
        players.sort(reverse=True)
        p=t=0
        matche=0
        while p<len(players) and t<len(trainers):
            if players[p]<=trainers[t]:
                matche+=1
                p+=1
                t+=1
            else:
                p+=1
        return matche


        