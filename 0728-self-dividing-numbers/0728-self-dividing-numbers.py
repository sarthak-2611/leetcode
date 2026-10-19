class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def is_sd(n):
            t = n
            while t:
                if not (d := t % 10) or n % d: return False
                t //= 10
            return True
            
        return [n for n in range(left, right + 1) if is_sd(n)]


