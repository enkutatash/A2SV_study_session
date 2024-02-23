class MinStack:

    def __init__(self):
        self.head=[]
        

    def push(self, val: int) -> None:
        self.head.append(val)
            
        

    def pop(self) -> None:
        self.head.pop()
        

    def top(self) -> int:
        return self.head[-1]
        

    def getMin(self) -> int:
        return min(self.head)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()