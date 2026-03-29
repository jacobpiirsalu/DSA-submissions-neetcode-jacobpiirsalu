class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = 0
        lens = list(map(lambda x: len(x), strs))
        leader = strs[0][0:r]
        while r<=min(lens):
            leader = strs[0][0:r]
            print(leader)
            for s in strs:
                if s[0:r] != leader:
                    return strs[0][0:r-1]
            r+=1

        return leader
