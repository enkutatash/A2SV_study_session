class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        takes=float("-inf")
        
        for i in range(0,len(tasks),4):
            t=processorTime[i//4]
            done=t+max([tasks[i],tasks[i+1],tasks[i+2],tasks[i+3]])
            takes=max(takes,done)
        return takes
            
        

        