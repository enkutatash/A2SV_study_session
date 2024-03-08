class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leading = []
        self.person = defaultdict(int)
        self.times = times
        

        for i in range(len(times)):
            self.person[persons[i]]+=1
            maxi = max(self.person.values())
            winner = []
            for j,v in self.person.items():
                if v==maxi:
                    winner.append(j)
                    print(j,v)
            if len(winner)>1:
                if self.person[persons[i]] == maxi:
                    self.leading.append(persons[i])
                else:
                    self.leading.append(self.leading[-1])
            else:
                self.leading.append(winner[0])
            
            
    def q(self, t: int) -> int:
        idx = bisect_left(self.times,t)
        if idx < len(self.times) and self.times[idx]==t:
            return self.leading[idx]
        else:
            return self.leading[idx-1]
       

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)