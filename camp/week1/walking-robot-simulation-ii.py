class Robot:

    def __init__(self, width: int, height: int):
        self.height=height
        self.width=width
        self.dirs={0:"East",1:"North",2:"West",3:"South"}
        self.dir=0
        self.move=[0,0]
        self.start=False

    def step(self, num: int) -> None:
        num=num%(2*self.height+2*self.width-4)
        self.start=True
        while num>0:
            if self.move==[self.width-1,0]:
                self.dir=1
            elif self.move==[self.width-1,self.height-1]:
                self.dir=2
            elif self.move==[0,self.height-1]:
                self.dir=3
            elif self.move==[0,0]:
                self.dir=0
            if self.dir==0:
                self.move[0]+=1
            elif self.dir==1:
                self.move[1]+=1
            elif self.dir==2:
                self.move[0]-=1
            elif self.dir==3:
                self.move[1]-=1
            num-=1
       

    def getPos(self) -> List[int]:
        return self.move
        

    def getDir(self) -> str:
        if self.move==[0,0] and self.start==True :
            return "South"
        return self.dirs[self.dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()