class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=']':
                stack.append(i)
            else:
                temp=[]
                while stack[-1]!='[':
                    last=stack.pop()
                    temp.append(last)
                stack.pop()
                mul=""
                if stack:
                    while stack and stack[-1].isdigit()==True:
                        mul+=stack.pop()
                    mul=mul[::-1]
                    temp=temp[::-1]*int(mul)
                stack.append("".join(temp))
        return "".join(stack)



        