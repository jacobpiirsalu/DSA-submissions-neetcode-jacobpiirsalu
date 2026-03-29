import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = list(string.ascii_lowercase + string.digits)


        forward = ''.join(c.lower() for c in s if c.lower() in alphanum)
        print(forward)
        backward = forward[::-1]

        return forward == backward
        