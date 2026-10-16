class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
           while n % 2 == 0: n //= 2  # Strip all factors of 2
           ans, d = 1, 3
           while d * d <= n:
              c = 0
              while n % d == 0: c, n = c + 1, n // d
              ans, d = ans * (c + 1), d + 2
           return ans * 2 if n > 1 else ans
        