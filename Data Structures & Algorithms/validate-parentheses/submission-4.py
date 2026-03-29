class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: 
            return False

        stack = []
        for i in range(len(s)):
            bracket = s[i]
            top = ""
            if stack:
                top = stack[-1]
            match bracket:
                case ")":
                    if top != "(":
                        return False
                    stack.pop()
                case "}":
                    if top != "{":
                        return False
                    stack.pop()
                case "]":
                    if top != "[":
                        return False
                    stack.pop()
                case _:
                    stack.append(bracket)
                    
        return len(stack)==0

        