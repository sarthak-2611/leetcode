class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
      w = s.split()
      return len(pattern) == len(w) and len(set(pattern)) == len(set(w)) == len(set(zip(pattern, w)))
        