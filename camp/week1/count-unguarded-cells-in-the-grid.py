class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        visited=set()
        dir_=[[0,1],[0,-1],[1,0],[-1,0]]
        walls=set(map(tuple,walls))
        guards=set(map(tuple,guards))
        
        for i, j in guards:
            for dx, dy in dir_:
                x,y=i,j
                while 0<=x<m and 0<=y<n and (x,y) not in walls:
                    if [x,y]!=[i,j] and (x,y) in guards:
                        break
                    visited.add((x,y))
                    x+=dx
                    y+=dy
        
        return (m*n)-(len(visited)+len(walls))

        

        