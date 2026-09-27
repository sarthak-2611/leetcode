class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []
        
        while i >= 0 or j >= 0 or carry:
            d1 = ord(num1[i]) - 48 if i >= 0 else 0
            d2 = ord(num2[j]) - 48 if j >= 0 else 0
            
            total = d1 + d2 + carry
            carry = 1 if total > 9 else 0
            res.append(chr((total % 10) + 48))
            
            i, j = i - 1, j - 1
            
        return "".join(res[::-1])
        