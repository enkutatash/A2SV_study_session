class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                curr=0
                while len(stack):
                    k=stack.pop()
                    if k=='(':
                        break
                    curr+=k
                if curr==0:
                    stack.append(1)
                else:
                    stack.append(curr*2)

        return sum(stack)
        