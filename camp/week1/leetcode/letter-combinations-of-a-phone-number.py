class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combination = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        ans = []
        curr = []
        def combine(i):
            if len(curr)==len(digits):
                curr2="".join(curr)
                if curr2!="":
                    ans.append(curr2)
                return
            if i>=len(digits) :
                return
            for k in range(len(combination[digits[i]])):
                curr.append(combination[digits[i]][k])
                combine(i+1)
                curr.pop()
                
        combine(0)
        return ans
        