class ATM:

    def __init__(self):
        self.current_amount=[0]*5
        self.notes=[20,50,100,200,500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.current_amount[i]+=banknotesCount[i]
        
        

    def withdraw(self, amount: int) -> List[int]:
        current=self.current_amount.copy()
        draw=[0]*5
        i=-1
        while amount>0:
            if i<-5:
                return [-1]
            if amount>=self.notes[i] and current[i]>0:
                needed=amount//self.notes[i]
                valid=min(needed,current[i])
                draw[i]+=valid
                amount-=(self.notes[i]*valid)
                current[i]-=valid

            else:
                i-=1
        self.current_amount=current.copy()
        return draw


        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)