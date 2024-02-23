class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        D=deque()
        R=deque()
        for i,v in enumerate(senate):
            if v=='R':
                R.append(i)
            else:
                D.append(i)
        
        while D and R :
            if D[0]<R[0]:
                R.popleft()
                z=D.popleft()
                D.append(z+n)
            else:
                D.popleft()
                z=R.popleft()
                R.append(z+n)
        if len(D)==0:
            return "Radiant"
        else:
            return "Dire"


        