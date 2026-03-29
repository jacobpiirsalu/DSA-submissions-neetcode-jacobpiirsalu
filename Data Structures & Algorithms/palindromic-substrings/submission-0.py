class Solution:
    def isPalindrome(self, s:str) -> bool:
        return s == s[::-1]
    def countSubstrings(self, s: str) -> int:
        count=0
        for windowSize in range(1,len(s)+1):
            l=0
            r=windowSize
            while r<=len(s):
                print(f'{l} : {r}')
                if self.isPalindrome(s[l:r]):
                    count+=1
                l+=1
                r+=1
        return count
        