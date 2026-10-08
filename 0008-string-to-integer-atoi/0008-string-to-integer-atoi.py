class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit signed integer limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        # If the string was empty or only contained spaces
        if i == n:
            return 0
            
        # 2. Check the sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i]) 
            
            
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            result = result * 10 + digit
            i += 1
            
        
        return sign * result

        