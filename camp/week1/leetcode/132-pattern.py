class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []

        for value in nums:
            if not stack:
                stack.append([value, value]) 
            elif stack[-1][0]>value:
                stack.append([value, value]) 
            else:
                Smallest=stack[-1][0]
                while stack and stack[-1][1]<value:
                    stack.pop()
                if stack and stack[-1][0]< value < stack[-1][1]:
                    return True
                stack.append([Smallest, value])
        return False
