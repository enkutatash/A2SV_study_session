class Solution:
    def interpret(self, command: str) -> str:
        s=''
        k=len(command)
        i=0
        while i<k:
            if command[i]=='(' and command[i+1]==')':
                s+='o'
                i+=2
            elif command[i]=='(' and command[i+1]!=')':
                s+='al'
                i+=4
            else:
                s+=command[i]
                i+=1
        return s
        