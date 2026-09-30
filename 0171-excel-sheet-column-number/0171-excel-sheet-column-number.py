class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
         return reduce(lambda res, c: res * 26 + ord(c) - 64, columnTitle, 0)
        