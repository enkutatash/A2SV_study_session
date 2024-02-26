class MyQueue:

    def __init__(self):
        self.stack=[]
        self.poped=[0]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if self.stack:
            end= self.poped.pop()
            self.poped.append(end+1)
            return self.stack[end]


        

    def peek(self) -> int:
        return self.stack[self.poped[-1]]
        

    def empty(self) -> bool:
        if (self.poped[-1]>=len(self.stack)) or(len(self.stack)==0):
            return True
        return False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()