class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0: n //= 4
        if n % 8 == 7: return 4
    
        is_sq = lambda x: int(math.isqrt(x))**2 == x
        if is_sq(n): return 1
        if any(is_sq(n - i*i) for i in range(1, int(math.isqrt(n)) + 1)): return 2
    
        return 3