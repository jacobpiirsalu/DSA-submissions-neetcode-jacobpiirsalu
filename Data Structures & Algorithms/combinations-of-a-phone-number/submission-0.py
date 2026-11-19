class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        ret = [""]
        hmap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        for digit in digits:
            tmp = []
            for nodeStr in ret:
                for char in hmap[digit]:
                    tmp.append(nodeStr+char)
            ret = tmp
        return ret
