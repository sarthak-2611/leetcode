class Solution:
    def convertToBase7(self, num: int) -> str:
        return '-' + self.convertToBase7(-num) if num < 0 else (self.convertToBase7(num // 7) + str(num % 7) if num >= 7 else str(num))
        