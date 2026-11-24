class Solution:
    def calculate(self, s: str) -> int:
        #/* first, then +/-
        stk = [0]
        prevVal = 0
        prevOp = "+"
        i=0
        while i<len(s):
            #print(stk)
            if s[i].isdigit():
                num=""
                while i<len(s) and s[i].isdigit():
                    #print(num)
                    num+=s[i]
                    i+=1
                #print(num)
                
                num = int(num)
                prevVal = stk[-1]
                if prevOp == "*":
                    stk.pop()
                    stk.append(prevVal*num)
                elif prevOp == "/":
                    #print("hit this")
                    stk.pop()
                    if prevVal < 0 or num<0:
                        #print(abs(prevVal)//abs(num))
                        stk.append(-1* (abs(prevVal)//abs(num)) )
                    else:
                        #print("prevVal: " + str(prevVal) + " num: " + str(num)) 
                        stk.append(prevVal//num)
                    #print(stk)
                elif prevOp == "+":
                    stk.append(num)
                elif prevOp == "-":
                    #print(-num)
                    stk.append(-num)
                i-=1
            elif s[i] == "*":
                prevOp = "*"

            elif s[i]=="/":
                prevOp = "/"

            elif s[i]=="+":
                prevOp = "+"

            elif s[i]=="-":
                prevOp = "-"
            i+=1
        return sum(stk)