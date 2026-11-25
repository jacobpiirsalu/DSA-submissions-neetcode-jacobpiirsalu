class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        ret = []
        
        digitToChar = {
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h', 'i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z']
        }
        path = []
        def dfs(digitIdx: int):
            if digitIdx >= len(digits):
                ret.append("".join(path))
                return
            else:
                for char in digitToChar[digits[digitIdx]]: #digitToChar["3"] -> "def"
                    path.append(char)
                    dfs(digitIdx+1)
                    path.pop()




        dfs(0) #side effect, appends to ret
        return ret