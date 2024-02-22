class MyStack:

    def __init__(self):
        self.head=[]
        

    def push(self, x: int) -> None:
        self.head.append(x)
        

    def pop(self) -> int:
        return self.head.pop()
        

    def top(self) -> int:
        return self.head[-1]
        

    def empty(self) -> bool:
        return True if  len(self.head)==0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()