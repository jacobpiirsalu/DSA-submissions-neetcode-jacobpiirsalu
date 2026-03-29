class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<=len(s)-1:
                if s[l]!=s[r]: break
                count+=1
                l-=1
                r+=1
            
            #odd length palindrome case
            l,r = i,i+1
            while l>=0 and r<=len(s)-1:
                if s[l] != s[r]: break
                count+=1
                l-=1
                r+=1
        return count


