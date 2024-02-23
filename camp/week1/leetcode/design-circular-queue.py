class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.queue=[0]*k
        self.front=-1
        self.rear=-1
        self.capacity=0
        

    def enQueue(self, value: int) -> bool:
        if self.capacity<self.k:
            if self.front==-1:
                self.front+=1
            self.capacity+=1
            self.rear+=1
            if self.rear==self.k:
                self.rear=0
            self.queue[self.rear]=value

            return True
        else:
            return False
        
        

    def deQueue(self) -> bool:
        if self.capacity==0:
            return False
        self.front+=1
        self.capacity-=1
        if self.front==self.k:
            self.front=0
        return True
        

    def Front(self) -> int:
        if self.capacity==0:
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.capacity==0:
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        if self.capacity==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.capacity==self.k:
            return True
        return False

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()