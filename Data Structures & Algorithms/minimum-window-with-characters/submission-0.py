class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        tmap = {}
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)

        l=0
        have = 0 #number of unique characters that we've met the criteria for
        need = len(tmap)
        window = {}
        ret,retLen=(-1,-1), float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in tmap and window[c] == tmap[c]:
                have+=1
            while have == need:
                if (r-l+1) < retLen:
                    ret = (l,r)
                    retLen = r-l+1
                window[s[l]]-=1

                if s[l] in tmap and window[s[l]]<tmap[s[l]]:
                    have-=1
                l+=1
        
        
        if retLen != float('inf'): return s[ret[0]:ret[1]+1]
        else: return ""
            
