class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = []

        def generate():
            if curr.count('(')==curr.count(')') and curr.count(')')==n:
                ans.append("".join(curr))
                return
            
            
            if curr.count('(')<n: 
                curr.append('(')
                generate()
                curr.pop()
            if curr.count('(')>curr.count(')'):
                curr.append(')')
                generate()
                curr.pop()
        generate()
        return ans
        