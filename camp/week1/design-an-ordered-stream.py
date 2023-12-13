class OrderedStream:

    def __init__(self, n: int):
        self.stream=dict()
        self.ptr=0
        
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey]=value
        l=list()
        while self.ptr+1 in self.stream.keys():
            self.ptr+=1
            l.append(self.stream[self.ptr])
        return l
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)