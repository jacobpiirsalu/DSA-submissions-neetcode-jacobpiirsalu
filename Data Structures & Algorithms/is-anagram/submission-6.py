import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        cmap, tmap = {}, {}

        for c in s: cmap[c] = cmap.get(c,0) + 1
        for c in t: tmap[c] = tmap.get(c,0) + 1
        
        return tmap == cmap