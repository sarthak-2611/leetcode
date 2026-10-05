class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
           
     groups = {}
     for s in strs:
        
        count = [0] * 26
        for c in s:
            count[ord(c) - 97] += 1
        
       
        key = tuple(count)
        
       
        if key in groups:
            groups[key].append(s)
        else:
            groups[key] = [s]
            
     return list(groups.values())

        