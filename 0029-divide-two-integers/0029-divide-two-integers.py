class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
            
        is_negative = (dividend < 0) ^ (divisor < 0)
        dvd, dvs = abs(dividend), abs(divisor)
        ans = 0
        
        for i in range(31, -1, -1):
            if (dvd >> i) >= dvs:
                ans += 1 << i
                dvd -= dvs << i
                
   
        if is_negative:
            ans = 0 - ans
            
        return max(-2147483648, min(2147483647, ans))

