class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
            
        prev = list(range(len(word2) + 1))
        
        for i, c1 in enumerate(word1):
            curr = [i + 1] + [0] * len(word2)
            for j, c2 in enumerate(word2):
                curr[j + 1] = prev[j] if c1 == c2 else 1 + min(prev[j + 1], curr[j], prev[j])
            prev = curr
            
        return prev[-1]

        