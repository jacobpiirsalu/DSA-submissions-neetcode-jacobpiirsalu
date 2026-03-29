class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l=0
        for i in range(len(s)):
            if l<len(t) and s[i] == t[l]:
                l+=1
        return len(t)-l
