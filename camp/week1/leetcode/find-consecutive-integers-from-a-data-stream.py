class DataStream:

    def __init__(self, value: int, k: int):
        self.queue=deque()
        self.check=defaultdict(int)
        self.value=value
        self.k=k

        

    def consec(self, num: int) -> bool:
        if len(self.queue)<self.k-1:
            self.queue.append(num)
            self.check[num]+=1
            return False
        elif len(self.queue)==self.k-1:
            self.queue.append(num)
            self.check[num]+=1
            if len(self.check)==1 and self.value in  self.check:
                return True
            else:
                return False

        else:
            z= self.queue.popleft()
            self.check[z]-=1
            if  self.check[z]==0:
                del  self.check[z]
            self.queue.append(num)
            self.check[num]+=1
            if len(self.check)==1 and self.value in  self.check:
                return True
            else:
                return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)