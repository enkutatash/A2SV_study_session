class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        nameidx = 0       
        typedidx = 0      
        while nameidx <= len(name) and typedidx < len(typed):
            if nameidx < len(name) and typed[typedidx] == name[nameidx]:
                typedidx += 1
                nameidx += 1
            elif nameidx != 0 and typed[typedidx] == name[nameidx-1]:
                typedidx += 1
            else:
                return False
            
        return nameidx == len(name) 
        