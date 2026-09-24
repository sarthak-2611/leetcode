class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        available_letters = Counter(magazine)
        for char in ransomNote:
            if available_letters[char] <= 0:
                return False
            available_letters[char] -= 1
            
        return True
        