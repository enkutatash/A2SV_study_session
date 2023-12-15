class Bitset:

    def __init__(self, size: int):
        self.size=size
        self.bit=["0"]*size
        self.opposite=["1"]*size
        self.one_bit=0
    def fix(self, idx: int) -> None:
        if self.bit[idx]=="0":
            self.bit[idx]="1"
            self.one_bit+=1
            self.opposite[idx]="0"
        

    def unfix(self, idx: int) -> None:
        if self.bit[idx]=="1":
            self.bit[idx]="0"
            self.one_bit=max(0,self.one_bit-1)
            self.opposite[idx]="1"
           
    def flip(self) -> None:
        
       self.opposite,self.bit=self.bit,self.opposite
       self.one_bit=self.size-self.one_bit
        
        
    def all(self) -> bool:
        return self.one_bit==self.size
        

    def one(self) -> bool:
        return self.one_bit>0
        

    def count(self) -> int:
        return self.one_bit

    def toString(self) -> str:
        return "".join(self.bit)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()