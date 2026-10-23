class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(t.encode()) - sum(s.encode()))
        