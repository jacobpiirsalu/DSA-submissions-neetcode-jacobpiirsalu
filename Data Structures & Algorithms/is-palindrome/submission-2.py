import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = list(string.ascii_lowercase + string.digits)


        forward = s.lower()
        forwardLst = []
        for c in forward:
            if c in alphanum:
                forwardLst.append(c)
                
        forward = "".join(forwardLst)
        print(forward)
        backward = forward[::-1]

        return forward == backward
        