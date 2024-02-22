class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cross_check=Counter(s)
        added=set()
        stack=[]

        for i in s:
            cross_check[i]-=1
            if i in added:
                continue
            while stack and ord(stack[-1])>ord(i) and cross_check[stack[-1]]>0:
                l=stack.pop()
                added.remove(l)
            added.add(i)
            stack.append(i)

        return "".join(stack)



        
        