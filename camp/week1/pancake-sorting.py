class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result=list()
        turn=len(arr)
        while turn>1:
            turn_index=arr.index(turn) 
            if turn_index==turn-1: 
                turn-=1
                continue
            if turn_index!=0:
                arr[:turn_index+1]=reversed(arr[:turn_index+1])
                result.append(turn_index+1) 

            arr[:turn]=reversed(arr[:turn])
            result.append(turn)
            
            turn-=1 
        return result