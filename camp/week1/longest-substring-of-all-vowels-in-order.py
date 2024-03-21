class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans = 1
        i=0
        j=0
        n= len(word)
        check = {
            'a':set(),
            'e':set('a'),
            'i':{'a','e'},
            'o':{'a','e','i'},
            'u':{'a','e','i','o'},
        }
        sample = set()
        while i<n:
            sample = set(word[i])
            curr = word[i]
            j = i+1
            while j<n:
                if word[j] in check[curr]:
                    if len(sample)==5:
                        ans = max(ans,j-i)
                    break
                else:
                    sample.add(word[j])
                    curr = word[j]
                    j+=1
            if j<n:
                i=j
            else:
                break
        print(sample)
        if len(sample)==5:
            ans = max(ans,j-i)
        
        return ans if ans != 1 else 0



        