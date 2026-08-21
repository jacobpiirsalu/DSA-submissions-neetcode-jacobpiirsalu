class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")", "{":"}", "[":"]"}
        #keys are openBrackets, values are close brackets
        stack = []
        for char in s:
            #top = brackets[stack[-1]] if len(stack)>0 else "invalid"
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                if stack and brackets[stack[-1]] == char:
                    stack.pop()
                else: return False
        return len(stack) == 0
        # time complexity: O(n)
        # space complexity O(n)