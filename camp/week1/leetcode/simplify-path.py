class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        
        stack1=list()
        for i in path:
            if i=='..':
                if len(stack1)!=0:
                    stack1.pop()
                
            elif i=='' or  i=='.':
                continue
            else:
                stack1.append(i)
            
           
        return '/'+"/".join(stack1)