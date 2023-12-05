class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        oneRow=[]
        first=set(('q','w','e','r','t','y','u','i','o','p'))
        second=set(('a','s','d','f','g','h','j','k','l'))
        third=set(('z','x','c','v','b','n','m'))
        for i in words:
            l=set(j for j in i.lower())
            if first.union(l)==first or second.union(l)==second or third.union(l)==third:
                oneRow.append(i)
        return oneRow


        