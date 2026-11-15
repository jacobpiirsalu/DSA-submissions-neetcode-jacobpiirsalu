class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        currNum = 0
        prevop = "+"
        s = s.replace(' ', '')
        for i, char in enumerate(s):
            if char.isdigit():
                currNum = currNum*10 + int(char)
                # build the base 10 num in question
            if (not char.isdigit()) or i == len(s)-1:
                if prevop=="+":
                    stack.append(currNum)
                    
                elif prevop=="-":
                    stack.append(-currNum)
                elif prevop=="*":
                    prevNum = stack.pop()
                    stack.append(prevNum*currNum)
                elif prevop=="/":
                    prevNum = stack.pop()
                    stack.append(int(prevNum/currNum))
                currNum=0
                prevop = char


        return sum(stack)