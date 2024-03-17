class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new=[]
        for i in range(len(image)):
            image[i].reverse()
            k=[]
            for j in range(len(image[0])):
                if image[i][j]==0:
                    k.append(1)
                else:
                    k.append(0)
            new.append(k)
        return new
        