class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        de=deque([i,v] for i,v in enumerate(tickets))
        time=0
        while de:
            time+=1
            z,y=de.popleft()
            y-=1
            if y!=0:
                de.append([z,y])
            if z==k and y==0:
                break
        return time



        