class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        result = []
        operation=[]
        size = len(boxes)

        for i in range(size):
            if boxes[i]=='1':
                result.append(i)
                
        for i in range(size):
            mini=0
            for j in result:
                mini+=abs(i-j)
            operation.append(mini)

        return operation
        



        