class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        for c in s:
            print(c)
            t = t.replace(c,'',1)
        
        print(s)
        print(t)
        if t =='': return True
        return False
        