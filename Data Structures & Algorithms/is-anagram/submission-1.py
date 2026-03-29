import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len(s) != len(t): return False

        cmap = {char : 0 for char in string.ascii_lowercase} # character: numTimesSeen -> mem = O(26) = O(1)
        tmap = {char : 0 for char in string.ascii_lowercase}
        #print(cmap)
        for c in s:
            if c not in cmap:
                cmap[c] = 1
            else:
                cmap[c]+=1
        for c in t:
            if c not in tmap:
                tmap[c] = 1
            else:
                tmap[c]+=1
        
        
        for char in string.ascii_lowercase:
            if tmap[char] != cmap[char]:
                return False
        
        
        return True