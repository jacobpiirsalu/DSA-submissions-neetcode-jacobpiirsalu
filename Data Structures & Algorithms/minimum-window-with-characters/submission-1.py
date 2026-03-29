class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minWindow = float('inf')
        ret = ""
        wmap = {char:0 for char in t}
        tmap = {char: 0 for char in t}

        for char in t:
            tmap[char] +=1

        def valid():
            return all(wmap[c] >= tmap[c] for c in tmap)

        l, r = 0, 0
        grow = True

        while r < len(s) or not grow:
            if grow:
                if s[r] in wmap:
                    wmap[s[r]]+=1
                if valid():
                    if r-l + 1 < minWindow:
                        minWindow = r-l+1
                        ret = s[l:r+1]
                    grow = False
                r+=1
            else:
                if s[l] in wmap:
                    wmap[s[l]]-=1
                l+=1
                if valid():
                    if r-l < minWindow:
                        minWindow = r-l
                        ret = s[l:r]
                else:
                    grow = True

        return ret