class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least=[]
        mini=float("inf")
        string=list1 if len(list1)<=len(list2) else list2
        string2=list1 if len(list1)>len(list2) else list2
        for i in range(len(string)):
            if string[i] in string2:
                if string2.index(string[i])+i<mini:
                    least=[]
                    least.append(string[i])
                    mini=string2.index(string[i])+i
                elif string2.index(string[i])+i==mini:
                    least.append(string[i])
        return least

        