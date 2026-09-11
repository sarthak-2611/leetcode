class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
     if not strs: return ""
    
   
     s1, s2 = min(strs), max(strs)
    
     for i, char in enumerate(s1):
        if i >= len(s2) or char != s2[i]:
            return s1[:i]
            
     return s1
