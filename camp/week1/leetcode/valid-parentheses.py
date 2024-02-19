class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        right={
            ']':'[','}':'{',')':'('
        }

        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if len(stack)>0:
                    k=stack.pop()
                    if k!=right[i]:
                        return False
                else:
                    return False
        if len(stack)>0:
            return False
        return True
