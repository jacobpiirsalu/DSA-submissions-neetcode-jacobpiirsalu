class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        openToClose = {'(':')', '{':'}', '[':']'}
        stk = []
        for c in s:
            if c =='(' or c =='{' or c =='[':
                stk.append(c)
            if c == ')' or c== '}' or c == ']':
                if stk and c == openToClose[stk[-1]]:
                    stk.pop()
                else:
                    return False
        return len(stk) == 0

        

        
        return True