class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space=len(spaces)
        string_with_space=""
        for i in range(space):
            if i==0:
                string_with_space+=s[0:spaces[i]]+" "
        
            else:
                string_with_space+=s[spaces[i-1]:spaces[i]]+" "
        string_with_space+=s[spaces[-1]:]
        return string_with_space

        

        
        