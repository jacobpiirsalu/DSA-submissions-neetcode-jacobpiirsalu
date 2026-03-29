class Solution:
    # Top down DP solution (memoization) here to speed this up.
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {} #(txt1, txt2):value
        def dfs(txt1, txt2) -> int:
            count = 0
            #base cases
            if len(txt1)==0 or len(txt2)==0:
                return 0
            if len(txt1)==1 and len(txt2)>=1:
                if txt1 in txt2: return 1
                else: return 0
            if len(txt2)==1 and len(txt1)>=1:
                if txt2 in txt1: return 1
                else: return 0

            if txt1[0] == txt2[0]:
                if (txt1[1:],txt2[1:]) not in memo:
                    memo[(txt1[1:],txt2[1:])] = dfs(txt1[1:],txt2[1:])

                count+= 1 + memo[(txt1[1:],txt2[1:])]
            else:
                if (txt1[1:],txt2) not in memo:
                    memo[(txt1[1:],txt2)] = dfs(txt1[1:],txt2)
                if (txt1, txt2[1:]) not in memo:
                    memo[(txt1, txt2[1:])] = dfs(txt1, txt2[1:])

                count+=max(memo[(txt1[1:],txt2)], memo[(txt1, txt2[1:])])
            
            return count

            

        return dfs(text1,text2)
       
        