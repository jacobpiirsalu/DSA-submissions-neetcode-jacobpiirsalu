class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set()
        for c in s:
            if c not in chars:
                chars.add(c)
        
        max_size = 0
        for c in chars:
            curr_k = k
            curr_size = 0
            l,r = 0,0
            while l<=r and r < len(s):
                if s[r] == c and curr_k >= 0:
                    curr_size+=1
                    max_size = max(max_size, curr_size)
                    r+=1
                elif s[r] != c and curr_k > 0:
                    curr_size+=1
                    max_size = max(max_size, curr_size)
                    curr_k-=1
                    r+=1
                elif s[r] == s[l] and s[r] != c and curr_k==0:
                    r+=1
                    l+=1


                else:
                    if s[l] != c:
                        curr_k +=1
                    curr_size-=1
                    l+=1
        return max_size
                    



        