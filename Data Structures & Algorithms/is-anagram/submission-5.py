import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cmap = {char : 0 for char in string.ascii_lowercase} # character: numTimesSeen -> mem = O(26) = O(1)
        tmap = {char : 0 for char in string.ascii_lowercase}
        for c in s:
                cmap[c]+=1
        for c in t:
                tmap[c]+=1
        
        
        
        return tmap == cmap