class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} #{(i) : True/False}
        def recurse(i):
            if i==len(s):
                return True

            # Check memo
            if i in memo:
                return memo[i]

            for word in wordDict:
                if s[i:].startswith(word):
                    if recurse(i+len(word)):
                        memo[i] = True
                        return True
                    else: memo[i] = False
            
            memo[i]=False
            return False
        
        return recurse(0)
        