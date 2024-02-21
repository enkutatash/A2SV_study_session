class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        end=0
        stack=[]
        while end<len(tokens):
            if tokens[end]=='+':
                stack.append(int(stack.pop()+stack.pop()))
            elif tokens[end]=='-':
                a,b=stack.pop(),stack.pop()
                stack.append(int(b-a))
            elif tokens[end]=='*':
                stack.append(int(stack.pop()*stack.pop()))
            elif tokens[end]=='/':
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(tokens[end]))
            end+=1
        return stack.pop()