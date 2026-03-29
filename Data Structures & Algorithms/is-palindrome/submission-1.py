class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        forward = s.lower()
        forwardLst = []
        for c in forward:
            if c in alphanum:
                forwardLst.append(c)
                
        forward = "".join(forwardLst)
        print(forward)
        backward = forward[::-1]

        return forward == backward
        