class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        total_elements = 2 ** (n - 1)
        half_elements = total_elements // 2

       
        if k > half_elements:
            return 1 - self.kthGrammar(n, k - half_elements)

       
        return self.kthGrammar(n - 1, k)
