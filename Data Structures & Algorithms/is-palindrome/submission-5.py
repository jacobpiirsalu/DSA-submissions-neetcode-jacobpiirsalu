import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = string.ascii_lowercase + string.digits
        l = 0
        r = len(s) - 1

        while l<r:
            print(f'r: {r}, l: {l}')
            if s[r].lower() not in alphanum:
                print(s[r].lower())
                r-=1
                continue
            if s[l].lower() not in alphanum:
                l+=1
                continue
            
            if s[r].lower() != s[l].lower():
                return False

            r-=1
            l+=1
        print('here')
        
        return True


        