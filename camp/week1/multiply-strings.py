class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        Inum1=0
        Inum2=0
        for i in num1:
            Inum1=(Inum1*10)+(ord(i)-48)
        for i in num2:
            Inum2=(Inum2*10)+(ord(i)-48)
        product=Inum1*Inum2
        return f'{product}'

        