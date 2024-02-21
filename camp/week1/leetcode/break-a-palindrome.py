class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome=list(palindrome)
        org=palindrome[:]
        found=False
        lastA=0
        
        if len(palindrome)==1 :
            return ''
        for i in range(len(palindrome)):
            if palindrome[i]!='a':
                c=palindrome[i]
                palindrome[i]='a'
                if palindrome==palindrome[::-1]:
                    palindrome[i]=c
                    continue
                break
            else:
                if i!=0 :
                    found=True
                    lastA=max(lastA,i)
                    
        
        if palindrome==org and found:
            palindrome[lastA]='b'
            


        k="".join(palindrome)

        return k if k!=org else ''
