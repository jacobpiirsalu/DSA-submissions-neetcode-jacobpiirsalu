class Solution:
    def isPalindrome(self, s: str) -> bool:
        # optimal space complexity solution, 2 pointers comparing in place

        L,R = 0, len(s)-1

        while L < len(s) and R >=0:
            if not s[L].isalnum():
                L+=1
                continue
            if not s[R].isalnum():
                R-=1
                continue
            if s[L].lower()!=s[R].lower():
                return False
            L+=1
            R-=1
        return True